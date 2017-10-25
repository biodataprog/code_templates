#!/usr/bin/env python3
genes = ['SOD1','CDC11','YFG1']
print(genes)
sort_genes = sorted(genes)
print(sort_genes)
numbers = [141, 7, 90, 3, 13]
print("unsorted",numbers)
numbers.sort()
print("sorted",numbers)
print("reversed",sorted(numbers,reverse=True))

alphanumbers = ['141', '7', '90', '3', '13']
print("Alphanumeric strings",alphanumbers)
print("Alpha sorted numbers",sorted(alphanumbers))
print("Numberic sorted",sorted(alphanumbers,key=int))
