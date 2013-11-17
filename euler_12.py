# -*- coding: utf-8 -*-
"""solve 12"""

import math

def triangular(arg):
    """triangular number"""
    return arg * (arg + 1) / 2

def divisor(arg):
    result = []
    for i in range(1, int(arg) + 1):
        if arg % i == 0:
            result += [i]
    return result

def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i is 0:
            yield i
            if i is not n / i:
                large_divisors.insert(0, n / i)
    for divisor in large_divisors:
        yield divisor

#print list(divisorGenerator(100))

n = 8

while True:
    if len(list(divisorGenerator(triangular(n)))) > 500:
        print n, triangular(n)
        break
    n += 1
    print n

print "All!"
