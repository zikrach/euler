# -*- coding: utf-8 -*-
"""solve 13"""

sum = 0

with open("13.txt", "r") as file:
    for line in file:
        sum += int(line)

print str(sum)[:10]
