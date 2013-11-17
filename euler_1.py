# -*- coding: utf-8 -*-
"""solve problem 1"""

s = 0

for x in xrange(3, 1000):
    if x % 5 == 0 or x % 3 == 0:
        s += x
print s
