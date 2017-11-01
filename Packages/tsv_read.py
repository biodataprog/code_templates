#!/usr/bin/env python3

import csv
with open('some.tsv') as f:
    reader = csv.reader(f,delimiter="\t")
    for row in reader:
        print("First col is ",row[0])
        print("Second col is ",row[1])
        print(row)
