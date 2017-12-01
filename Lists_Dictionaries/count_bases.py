#!/usr/bin/env python3
dna =  'AAGAGAGGATACA'
bases = {'A':0, 'C':0, 'G':0, 'T':0 }
for l in dna:
    bases[l] += 1

print(bases)
