# -*- coding: utf-8 -*-
"""solve problem 2"""


n = 1
m = 1
result = 0

while n < 4000000:
    s = n + m
    n = m
    m = s
    if s % 2 == 0:
        result += s
print result
    

