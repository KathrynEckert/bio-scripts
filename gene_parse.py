import os
import argparse
import re
import sys
import time

FILE_NAME_FORMAT = r"\w+\.txt$"

def find_pattern_content(sequence, pattern) -> float:
    total = len(sequence)
    if(total == 0):
        return 0

    expression = rf"[{pattern}]"
    count = len(re.findall(expression, sequence))
    final = round((count / total) * 100, 1)  # percentage rounded to 1 decimal pt
    
    print(f"\nPattern {pattern} content: {final}")
    return final

def transcribe(name, sequence):
    sequence = sequence[::-1]
    transcription_map = {"A" : "U", "T" : "A", "G" : "C", "C": "G"}
    for i, c in enumerate(sequence):
        if c in transcription_map:
            sequence = sequence[:i] + transcription_map[c] + sequence[i+1:]
    third_ad(sequence)

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
    return mapper

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

    with open(os.path.join(args.target, f)) as file:
        sequence += file.read()

    print(f"\n### Analyzing File {f} ###")
    average += find_pattern_content(sequence, pattern)
    transcribe(f, sequence)
    print("\n##########################")

time_stop = time.time()
print(f"Processed {num_files} files in {time_stop-time_start} seconds.")
print(f"Results located in ./{args.output}")

