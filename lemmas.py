#! /usr/bin/env python3
"""
Build lemmas document contents from other tex files.

Run with -h for more information.
"""
from collections import namedtuple
import argparse
import os

# Input directory
idir = "sections" + os.sep

# Output file name
ofname = "lemmas_content.tex"

# Argument parsing
parser = argparse.ArgumentParser(description="Builds lemmas document content from\
section tex files as well as the theorems tex file. Output is written to " + ofname + ".")
args = parser.parse_args()

def get_arg(line, cmd) :
    """
    Retuns the argument if the Latex cmd
    is found. Otherwise None is returned.
    """
    lcmd = "\\" + cmd + "{"
    if line.find(lcmd) != 0 :
        return None
    j = line.find("}")
    if j < 0 :
        return None
    return line[len(lcmd):j]

sargs = ("lem", "cor", "defin", "thrm")
counter_map = {"section" : "chapter",
           "subsection" : "section"}
def process_file(fpath, ofile, headers=False, shared=None) :
    """
    Processes latex file to extract statements
    
    fpath - Path to .tex file
    ofile - Output file object
    headers - Increment counters for header lines
    shared - Name of shared statement file we are
             reading (None indicates we are not in
             a shared statement)
    """
    # Open up input file for reading
    with open(fpath, "r") as ifile :
        # Whether or not we are in a statement or comment block
        ins = False
        inc = False
        mdef = 0

        # Go through each line in the file
        for line in ifile :
            # We don't care about whitespace at the beginning or end of the line
            sl = line.strip()

            # Are we in a commented out block?
            if inc :
                if sl.find(r"\fi") == 0 :
                    inc = False
                continue

            # Are we in a statement block?
            if ins :
                # Pass the line through
                print(sl, file=ofile)

                # Are ending the statement?
                if get_arg(sl, "end") in sargs :
                    # Print a blank line to leave some spaces
                    print("", file=ofile)
                    ins = False
            else :
                # No, only pass through certain lines pertaining to the statements
                earg = get_arg(sl, "exercise")
                iarg = get_arg(sl, "input")
                scarg = get_arg(sl, "setcounter")
                if (sl.find(r"\def") == 0 and sl.find("{") >= 0) or mdef > 0 :
                    # Include any macro definitions
                    print(sl, file=ofile)
                    if sl[-1] == "{" :
                        # Multiline def
                        mdef += 1
                    elif sl[0] == "}" :
                        # End multiline def
                        mdef -= 1
                elif sl.find(r"\iffalse") == 0:
                    # Start of comment block
                    inc = True
                    continue
                elif earg :
                    # Exercise line, set counters
                    e = int(earg)
                    print(r"\setcounter{section}{" + str(e-1) + "}\stepcounter{section}", file=ofile)
                elif iarg and iarg.find("shared") == 0 :
                    # Input line for shared satement
                    process_file(iarg + ".tex", ofile, shared=iarg.split("/")[-1])
                elif get_arg(sl, "begin") in sargs :
                    # We are starting a statement, verify that no content is also on this line
                    if sl[-1] != "}" :
                        raise ValueError("Statement has content on the same line!")

                    add = ""

                    # Add shared tag if applicable
                    if shared :
                        add += "[Shared: " + shared.replace("_", r"\textunderscore ") + "] "

                    # Determine the label tag (if there is one)
                    lbl = "label"
                    i = sl.find("\\" + lbl)
                    if i >= 0 :
                        larg = get_arg(sl[i:], lbl)
                        if larg :
                            add += r"\{" + larg + r"\}"
                    print(sl + add, file=ofile)

                    ins = True
                elif scarg :
                    # Set counter line
                    print(sl.replace(scarg, counter_map[scarg]), file=ofile)
                elif headers :
                    # Search for counter lines to increment counters
                    for hdr in counter_map.keys() :
                        if sl.find("\\" + hdr) == 0 :
                            print(r"\stepcounter{" + counter_map[hdr] + "}", file=ofile)

# Section file record
Section = namedtuple("Section", ("sec", "fname"))
                    
# Open up output file for writing
with open(ofname, "w") as ofile :
    # Go through files in the current directory
    secs = []
    for fname in sorted(os.listdir(idir)) :
        # We only care about certain tex files
        (bname, ext) = os.path.splitext(fname)
        if ext != ".tex" :
            continue
        if bname.find("sec_") != 0 :
            continue
        secs.append(Section("_".join(bname.split("_")[1:]), idir + fname))

    # Sort sections and go through them
    print(r"\section{Solutions}", file=ofile)
    for sec in sorted(secs, key=lambda s : s.sec) :
        print("Processing " + sec.fname + "...")

        # Is this a special section with text?
        tsec = False
        try :
            slab = int(sec.sec)
        except :
            slab = sec.sec.split("_")[1]
            tsec = True
        
        # Set section counter
        if not tsec :
            # Normal numbered section
            print(r"\setcounter{chapter}{" + str(slab) + "}", file=ofile)
        else :
            # Special text section
            print(r"\renewcommand\thechapter{" + slab + "}", file=ofile)

        # Process section file
        process_file(sec.fname, ofile)

        # If text section the restore numbered sections
        if tsec :
            print(r"\renewcommand\thechapter{\arabic{chapter}}", file=ofile)
