# Day 1: Sonar Sweep (Part One)
# Author: Anna Wilhelm

import sys

count = 0
one_before = int(sys.stdin.readline())
for line in sys.stdin:
    number = int(line)
    if number > one_before:
        count +=1
    one_before = number
print(count)

    

    

