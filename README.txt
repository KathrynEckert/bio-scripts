A script for proccesing Yeast Genes for BIOL-130
Adapted from an original script (myGeneParser.py) by Dr. Babbitt

Details:
This script attempts to analyze sequence files for frequency of a provided pattern.
It prints these results to the terminal and generates a summary file in a provided output directory.
If desired, the flag -detailLogs or -d can be passed to include a summary file for each file processed.

For ease of use, the default values are as below:
target='YeastGenes' (exits gracefully if directory not found)
output='GeneParseResults' (will create if doesn't exist)
match='gc'
detailLogs is off by default

Call -help for more information on the available options.

The goal of this script was to imitate the original in function while providing more customization
through command line options and convert some of the code to a more pythonic style. Time comparisons
indicated it performs roughly the same (excluding file writing, which the original does not do) with
slightly more overhead due to use of regular expressions for flexibility with the pattern matching.
