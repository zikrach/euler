# -*- coding: utf-8 -*-
"""solve problem 7"""

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

for i in xrange(2, 10001 * 10001):
    if prime(i):
        k += 1
    if k == 10001:
        print i
        break

print "All!!!"
