# Day 1: Sonar Sweep (Part Two)
# Author: Anna Wilhelm

import sys

measurements = []
for line in sys.stdin:
    measurements.append(int(line))

previous_sum = measurements[0] + measurements[1] + measurements[2]
current_sum = 0
counter = 0

for i in range(1, len(measurements)-2):
    current_sum = measurements[i] + measurements[i+1] + measurements[i+2]
    if current_sum > previous_sum:
        counter = counter + 1
    previous_sum = current_sum
print(counter)

    

    

