# -*- coding: utf-8 -*-
"""solve 16"""

number = 2 ** 1000
string = str(number)
result = 0

for i in string:
    result += int(i)

print result
