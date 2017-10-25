#!/usr/bin/env python3
import itertools
import sys
import re
def isheader(line):
    return line[0] == '>'

def aspairs(f):
    seq_id = ''
    sequence = ''
    for header,group in itertools.groupby(f, isheader):
        if header:
            line = next(group)
            seq_id = line[1:].split()[0]
        else:
            sequence = ''.join(line.strip() for line in group)
            yield seq_id, sequence

CDS_file = "CDS.fa"
codon_table_file = 'codon_table.txt'
codon2protein = {}

with open(codon_table_file, "r") as fh:
    for line in fh:
        cols = line.split("\t")
        codon2protein[cols[0]] = cols[1]

print(codon2protein)
with open(CDS_file, "r") as cdsfh:
    seqs = dict(aspairs(cdsfh))

for id in seqs:
    print ("seq id is ",id)
    cds = seqs[id]
    protein_seq = ''
    print("is this divisible by 3?: ", len(cds), len(cds) % 3)
    for i in range(0,len(cds),3):
        codon = cds[i:i+3]
        aa = codon2protein[codon]
#        print(codon, aa)
        protein_seq += aa

print( "final sequence is")
print(protein_seq)
