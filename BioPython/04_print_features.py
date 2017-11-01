#!/usr/bin/env python3
import sys
import Bio
from Bio import SeqIO
from Bio.Seq import Seq
    

# seqfile 
if len(sys.argv) != 2:
    print("argument should be\n","02_parse_seq.py AJ240084.gbk")
    exit()

filename = sys.argv[1]
for seq_record in SeqIO.parse( filename , "genbank"):
    print(seq_record.id)
    for feature in seq_record.features:
        print("\t",feature.type,feature.location)
        print("\t",feature.type,feature.location.start,
              feature.location.end, feature.location.strand)
        if feature.type == "5'UTR":
            print(seq_record.seq[feature.location.start:feature.location.end])
