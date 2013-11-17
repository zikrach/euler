# -*- coding: utf-8 -*-
"""solve problem 10"""

import math

def prime(self):
    """if number is prime"""
    result = True
    for i in xrange(2, int(math.sqrt(self)) + 1):
        if self % i == 0:
            result = False
            break
    return result

k = 0

for i in xrange(2, 2000000):
    if prime(i):
        k += i

print k
print "All!!!"