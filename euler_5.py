# -*- coding: utf-8 -*-
"""solve problem 5"""

number = 11

for i in xrange(12, 20):
    number *= i

for num in xrange(2, number):
    k = True
    for i in xrange(11, 20):
        if (num * 2520) % i != 0:
            k = False
            print "No", num
            break
    if k:
        print num * 2520
        break
print "All!"

for i in xrange(11, 20):
    print (num * 2520) % i
