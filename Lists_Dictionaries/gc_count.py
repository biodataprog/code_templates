#!/usr/bin/env python3
import sys

def percentage_bases (base_counts):
    total_base_count = 0
    percentages = {}
    for nt, count in base_counts.items():
        total_base_count += count
        print("base is ",nt, " count is ",count)
    for nt, count in base_counts.items():
        percentages[nt] = 100 * (count / total_base_count)

    return percentages

def gc_content (base_counts):
    total_base_count = 0
    percentages = {}
    for nt, count in base_counts.items():
        total_base_count += count
        print("base is ",nt, " count is ",count)
    gc = 100 * ( base_counts['G'] + base_counts['C'] ) / total_base_count
    return gc
    
dna =  'AAGAGAGGATACA'
dna = ""
dna = ''.join(line.strip() for line in sys.stdin)


bases = {} # or initialize to 0 { 'A':0, 'C':0, 'G':0, 'T':0 }

for base in dna:
    if base in bases:
        bases[base] += 1
    else:
        bases[base] = 1
        
print(bases)

pcts = percentage_bases(bases)
print(pcts)

gcreturned = gc_content(bases)
print("this sequence has GC content of {}".format(gcreturned))

# we want this to take in a dictionary of base counts
# and return a dictionary with % of each base


#bases = {}
#bases['A'] = 0
#if 'A' in bases:
#    print("hello")
#print(bases)
