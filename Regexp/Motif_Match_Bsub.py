#!/usr/bin/env python3
#Python code to demonstrate pattern matching

# import the regular expression library
import re

# a random DNA sequence generator
def read_DNA (file):
    DNA = ""
    fasta_pat = re.compile(">")

    with open(file, 'r') as f:
        seenheader = 0 
        for line in f:
            if fasta_pat.search(line):
                if seenheader:
                    return DNA
                print("Header matches",line);
                seenheader = 1
            else:
                DNA += line
        DNA = re.sub("\s+","",DNA)
    return DNA

    


# lets initialize a pattern we want to match
# let's use the PRE motif which is a binding site for
# a transcription factor
# based on this paper:
# 

EcoRI   = "GAATTC" 
Bsu15I  = "ATCGAT"  
Bsu36I  = "CCT[ACGT]AGG"
BsuRI   = "GGCC"
EcoRII  = "CC[AT]GG"

RestrictionEnzymes = [EcoRI, Bsu15I, Bsu36I,
                      BsuRI, EcoRII]

# Now let's search for this element in DNA sequence

DNA = read_DNA("B_subtilis_str_168.fasta")
print("Bsub DNA is", len(DNA), "bp long")
for RE in RestrictionEnzymes:
    pattern = re.compile(RE)
    match = pattern.search(DNA)
    count = pattern.findall(DNA)
    print(RE,"matches", len(count), "sites")
#    while match:
#        print match.group(0), match.start(), match.end()
#        match = pattern.search(DNA,match.end()+1)

    print("//")


DNA = read_DNA("Ecoli_K-12.fasta")
print("Ecoli DNA is", len(DNA), "bp long")
for RE in RestrictionEnzymes:
    pattern = re.compile(RE)
    match = pattern.search(DNA)
    count = pattern.findall(DNA)
    print(RE,"matches", len(count), "sites")
#    while match:
#        print match.group(0), match.start(), match.end()
#        match = pattern.search(DNA,match.end()+1)

    print("//")




