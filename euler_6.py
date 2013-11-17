# -*- coding: utf-8 -*-
"""solve problem 6"""

sum = 1
kvadr = 1

for i in xrange(2, 101):
    sum += i * i
    kvadr += i
print sum
print kvadr

result = sum - (kvadr * kvadr)
print result
