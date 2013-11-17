# -*- coding: utf-8 -*-
"""solve problem 4"""


def palindrom(args):
    result = False
    string = str(args)
    string2 = string[len(string) / 2:]
    if len(string) % 2 == 0 and string[:len(string) / 2] == string2[::-1]:
        result = True
    return result
s = 1

for i in xrange(999, 1, -1):
    for j in xrange(999, 1, -1):
        if i * j > s and palindrom(i * j):
            s = i * j
            print i, j, s
