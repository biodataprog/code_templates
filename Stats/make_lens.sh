#!/usr/bin/bash
gunzip *.fa.gz

./sequence_length.py transposon.fa > transposon.lengths
./sequence_length.py mRNA.fa > mRNA.lengths

