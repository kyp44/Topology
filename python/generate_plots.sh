#!/bin/bash

# Run scripts that product plots
python3 ex_2.6_plots.py

# Move plots to figure directory
mv *.pdf ../figs/
