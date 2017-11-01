#!/usr/bin/env python3
import sys
import Bio
from Bio import SeqIO
from Bio.Seq import Seq
    

# seqfile 
if len(sys.argv) != 2:
    print("argument should be\n","02_parse_seq.py E3Q6S8.fasta")
    exit()

filename = sys.argv[1]
for seq_record in SeqIO.parse( filename , "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(seq_record.seq)
    print(len(seq_record))
