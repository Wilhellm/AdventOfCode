# Day 2: Dive! (Part 2)
# Author: Anna Wilhelm

import sys

horizontal = 0
depth = 0
aim = 0
for line in sys.stdin:
    s = line.split(' ')
    directions = s[0]
    units = int(s[1])
    if directions == "forward":
        horizontal = horizontal + units
        
    elif directions == "down":
        depth = depth + units
    else:
        depth = depth - units
print(horizontal*depth)


    

    

