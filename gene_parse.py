import os
import argparse
import re
import sys
import time

FILE_NAME_FORMAT = r"\w+\.txt$"

parser = argparse.ArgumentParser()
parser.add_argument('-target', '-t', default='YeastGenes')
parser.add_argument('-output', '-o', default='GeneParseResults')
parser.add_argument('-match', '-m', default='gc')
args = parser.parse_args()
# could add an option to overwrite found duplicates?

if not os.path.isdir(args.target):
    print(f"ERROR: Directory {args.target} not found")
    sys.exit()

if not os.path.isdir(args.output):
    os.mkdir(args.output)

file_count = 0
pattern = args.match.upper()
average = 0
num_files = 0
time_start = time.time()

for f in os.listdir(args.target):
    if not re.match(FILE_NAME_FORMAT, f):
        continue  # skip files with unexpected names

    num_files += 1
    sequence = ""

    with open(f) as file:
        sequence += file.read()

    # find matches and add to average
    # transcribe

    # need filename
    # need sequence therein

time_stop = time.time()
print(f"Processed {num_files} files in {time_stop-time_start} seconds.")
print(f"Results located in ./{args.output}")

