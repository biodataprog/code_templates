#!/usr/bin/env python3
import sys
counter = 0
char_count = 0

# replace \r with \n in a file

for line in sys.stdin:
    line_char_count = 0
    line = line.strip()
    print(line)
    print("line has ",len(line)," characters")
    counter += 1
    char_count += len(line)

print ("There are",counter, "lines and", char_count, "characters")
