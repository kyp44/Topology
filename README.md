Topology by James Munkres, 2nd Edition
======================================

Solutions Manual
----------------

The main solutions manual is `solutions.tex`.
Some solutions have figures, which are the `.pdf` files in the `figs` directory.
Most of these figures were created with the `xfig` program, whose `.fig` source files are also in the `figs` directory.
Some of the figures, however, are plots, which were generated with Python and Matplotlib.
To generate these figures and install them to the `figs` directory change to the `python` directory and run the `generate_plots.sh` script.
The `python` directory also contains some quick and dirty Python scripts that were used to gain insight while working on some of the exercises.
These are not really documented at all and so probably will not be of interest to anyone else.

When doing exercises it can be useful to see a list of lemmas that have been written as part of the solutions.
Running the `lemmas.py` Python script will build `lemmas_content.tex` that contains these lemmas.
You can then build a lemma list document by compiling `lemmas.tex`, which includes `lemmas_content.tex`.

If you are interested in contributing, send me a message.
Also, please submit an issue if you discover any errors in any of the proofs or any typos.

For an up-to-date PDF of the solutions manual and links to other solutions manuals for this text head over to [my website](https://kyp4.dyndns-home.com/topology/).
