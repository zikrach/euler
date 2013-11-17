# -*- coding: utf-8 -*-
"""solve problem 9"""

for a in xrange(1, 1000):
    for b in xrange(1, 1000):
        for c in xrange(1, 1000):
            if a + b + c == 1000 and a * a + b * b == c * c:
                print a, "^2+", b, "^2 = ", c, "^2"
                print a * b * c
print "All!"
