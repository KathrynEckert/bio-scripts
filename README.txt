A script for proccesing Yeast Genes for BIOL-130
Adapted from an original script (myGeneParser.py) by Dr. Babbitt

Details:
This script attempts to analyze sequence files for frequency of a provided pattern.
It prints these results to the terminal and generates a summary file in a provided output directory.
If desired, the flag -detailedLogs or -d can be passed to include a summary file for each file processed.

For ease of use, the default values are as below:
target='YeastGenes'
output='GeneParseResults'
match='gc'
And detailed logs is left off.

Call -help for more information on the available options.

The goal of this script was to imitate the original in function while providing more customization
through command line options and convert some of the code to a more pythonic style.
