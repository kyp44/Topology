Topology by James Munkres, 2nd Edition
======================================

Solutions Manual
----------------

The main solutions manual is `solutions.tex`.
Some solutions have figures, which are done directly in LaTeX using the [TikZ](https://www.ctan.org/pkg/pgf) and [PGFPLOTS](https://ctan.org/pkg/pgfplots) packages.
The `python` directory contains some quick and dirty Python scripts that were used to gain insight while working on some of the exercises.
These are not documented at all and so probably will not be of interest to anyone else.

Other Documents
---------------

When doing exercises it can be useful to see a list of lemmas that have been written as part of the solutions.
Running the `lemmas.py` Python script will build `lemmas_content.tex` that contains these lemmas.
You can then build a lemma list document by compiling `lemmas.tex`, which includes `lemmas_content.tex`.

Miscellaneous
-------------

Please submit an issue if you discover any errors in any of the proofs or any typos.

For an up-to-date PDF of the solutions manual and links to other resources for this text head over to [my website](https://math-study.net/topology/).
Note that this is still a work in progress.
