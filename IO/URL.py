#!/usr/bin/env python3

import urllib.request
orginfo = "https://biodataprog.github.io/programming-intro/data/random_exons.csv"
info = urllib.request.urlopen(orginfo)
for line in info:
    #linestrip = line
    linestrip = line.decode('UTF-8').strip()
    print(linestrip)
