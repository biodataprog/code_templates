#!/usr/bin/env python3
import re
EcoRI   = "GAATTC"
EcoRII  = "CC[AT]GG"
RestrictionEnzymes = [EcoRI, EcoRII]
DNA = "ACAGACGAGAGAATTCGGTAGAT"
for RE in RestrictionEnzymes:
   pattern = re.compile(RE)
   match = pattern.search(DNA)
   count = pattern.findall(DNA)
   print(RE,"matches", len(count), "sites")
   print("//")
