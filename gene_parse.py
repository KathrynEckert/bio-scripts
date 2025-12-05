import os
import argparse
import re
import sys
import time
from datetime import date

FILE_NAME_FORMAT = r"\w+\.txt$"

### ANALYSIS FUNCTIONS ###

def find_pattern_content(sequence, pattern) -> float:
    total = len(sequence)
    if(total == 0):
        return 0

    expression = rf"[{pattern}]"
    count = len(re.findall(expression, sequence))
    final = round((count / total) * 100, 1)  # percentage rounded to 1 decimal pt
    
    print(f"\nPattern {pattern} content: {final}")
    return final

def transcribe(sequence) -> dict:
    sequence = sequence[::-1]
    transcription_map = {"A" : "U", "T" : "A", "G" : "C", "C": "G"}
    for i, c in enumerate(sequence):
        if c in transcription_map:
            sequence = sequence[:i] + transcription_map[c] + sequence[i+1:]
    return third_ad(sequence)

def third_ad(sequence) -> dict:
    total = 0
    mapper = {"A": 0, "U": 0, "G": 0, "C": 0}
    for i in range(0, len(sequence), 2):
        if sequence[i] in mapper:
            total += 1
            mapper[sequence[i]] += 1
        i += i

    if total == 0:
        print("ERROR: unable to analyze third amino acid ratio")
    else:
        print("Codon 3rd Place Analysis:")
        for i in mapper:
            result = round(((mapper[i]/total)*100), 1)
            print(f"\t%{i} is {result}")
            mapper[i] = result  # replaces raw numbers with result since total is local
    return mapper

### ARGUMENT HANDLING ###

parser = argparse.ArgumentParser()
parser.add_argument('-target', '-t', default='YeastGenes')
parser.add_argument('-output', '-o', default='GeneParseResults')
parser.add_argument('-match', '-m', default='gc')
parser.add_argument('-summarize', '-s', default=True, choices=[True, False])
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

### RUN SCRIPT ###

for f in os.listdir(args.target):
    if not re.match(FILE_NAME_FORMAT, f):
        continue  # skip files with unexpected names

    num_files += 1
    sequence = ""

    with open(os.path.join(args.target, f)) as file:
        sequence += file.read()

    print(f"\n### Analyzing File {f} ###")
    pattern_content = find_pattern_content(sequence, pattern)
    average += pattern_content
    third_ad_res = transcribe(sequence)
    print("\nAnalysis complete. Writing file...")

    result_f = os.path.join(args.output, f)
    with open(result_f, 'w') as file:
        file.write(f"{f[:-4]} Sequence Analysis Report\n\n")
        file.write(f"Matching Pattern: {pattern}\n")
        file.write(f"Results: {pattern_content}%\n")
        file.write("\nThird Position Ratio Results:\n")
        for i in third_ad_res:
            file.write(f"\t{i}: {third_ad_res[i]}%\n")
    print("Complete.")
    print("\n##########################")

time_stop = time.time()
print(f"Processed {num_files} files in {time_stop-time_start} seconds.")
summary_loc = ""

if args.summarize:
    pattern_avg = round(average/num_files, 1)
    print(f"\nAverage Pattern Content: {pattern_avg}")
    summary_title = f"{args.target}_summary_{date.day}_{date.month}_{date.year}.txt" # datetime issue
    sum_file = os.path.join(args.output, summary_title)
    with open(sum_file, 'w') as file:
        file.write(f"Summary of Analysis on {args.target}\n\n")
        file.write(f"Numer of Files Analyzed: {num_files}\n")
        file.write(f"Pattern: {pattern}\n")
        file.write(f"Results: {pattern_avg}\n")
        file.write(f"\nTime elapsed: {round(time_stop-time_start, 3)} seconds")
    summary_loc = summary_title

print(f"Results located in ./{args.output}")
if args.summarize:
    print(f"Summary File: {os.path.join(args.output, summary_loc)}")

