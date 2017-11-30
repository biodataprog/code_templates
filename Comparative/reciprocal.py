#!/usr/bin/env python3

# blastp -query E_coli_K12.pep -db S_enterica.pep -outfmt 6 -evalue 1e-5 -num_threads 16 -out Ecol-vs-Sent.BLASTP
#blastp -query S_enterica.pep -db E_coli_K12.pep -outfmt 6 -evalue 1e-5 -num_threads 16 -out Sent-vs-Ecol.BLASTP

file1 = "Ecol-vs-Sent.BLASTP"
file2 = "Sent-vs-Ecol.BLASTP"

dictAB = {}
dictBA = {}

with open(file1,"r") as fh1:
    for line in fh1:
        line = line.strip() # remove trailing newline
        row = line.split("\t") # split line on tab to make list
        query = row[0]
        hit   = row[1]
        evalue = row[-2]
#        print(query,hit,evalue)
        # assume the first hit is the best one for a given query
        if not(query in dictAB):
            dictAB[query] = hit

with open(file2,"r") as fh1:
    for line in fh1:
        line = line.strip() # remove trailing newline
        row = line.split("\t") # split line on tab to make list
        query = row[0]
        hit   = row[1]
        evalue = row[-2]
       # print(query,hit,evalue)
        # assume the first hit is the best one for a given query
        if not(query in dictAB):
            dictBA[query] = hit

for seqA in dictAB:
    bestB_hit = dictAB[seqA]
    if bestB_hit in dictBA:
        bestA_hit = dictBA[bestB_hit]
        if seqA == bestA_hit:
            print(seqA,bestB_hit)
            


            
