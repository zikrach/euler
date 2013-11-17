# -*- coding: utf-8 -*-
"""solve problem 3"""

import math


def prime(self):
    """if number is prime"""
    result = True
    for i in xrange(2, int(math.sqrt(self)) + 1):
        if self % i == 0:
            result = False
            break
    return result


print prime(25)

number = 600851475143
print math.sqrt(number)

for i in xrange(2, int(math.sqrt(number)) + 1):
    if number % i == 0 and prime(i):
        print i
print "It is All!"
