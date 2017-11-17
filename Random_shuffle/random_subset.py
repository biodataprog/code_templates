#!/usr/bin/env python3
import sys, random
# read the filename from the cmdline
filename=sys.argv[1]
total_lines_wanted = 100000

with open(filename,"r") as fh:
    count_lines = 0
    lines = []
    #         fh.readlines()
    for line in fh:
        if not line[0] == "#":
            lines.append(line.strip())
            count_lines += 1
    for i in range(0,total_lines_wanted):
        index = random.randint(0,count_lines)
        print(lines[index])
#    print(len(lines)," length array")  
#    print("I saw ",count_lines,"lines")
