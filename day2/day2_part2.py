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
        depth = depth + aim*units
    elif directions == "down":
        aim = aim + units
    else:
        aim = aim - units
print(horizontal*depth)


    

    

