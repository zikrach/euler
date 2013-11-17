# -*- coding: utf-8 -*-
"""solve problem 11"""

i = 1
numbers = {}

with open("11.txt", "r") as file:
    for line in file:
        numbers[int(i)] = ['0', '0', '0', '0'] + line.strip().split(None, 20) + ['0', '0', '0', '0']
        i += 1

for i in xrange(0, -3, -1):
    numbers[int(i)] = []
    for j in xrange(1, 28):
        numbers[int(i)] += ['0']

for i in xrange(21, 24):
    numbers[int(i)] = []
    for j in xrange(1, 28):
        numbers[int(i)] += ['0']

print numbers

result = 1

for i in xrange(1, 21):
    for j in xrange(1, 21):
        prod1 = 1
        prod2 = 1
        prod3 = 1
        prod4 = 1
        prod5 = 1
        prod6 = 1
        prod7 = 1
        prod8 = 1
        for k in xrange(0, 4):
            prod1 *= int(numbers[i][j + k])
            prod2 *= int(numbers[i + k][j])
            prod3 *= int(numbers[i + k][j + k])
            prod4 *= int(numbers[i + k][j - k])
            prod5 *= int(numbers[i - k][j + k])
            prod6 *= int(numbers[i - k][j - k])
            prod7 *= int(numbers[i][j - k])
            prod8 *= int(numbers[i - k][j])
        if prod1 > result:
            result = prod1
            print i, j, result
        if prod2 > result:
            result = prod2
            print i, j, result
        if prod3 > result:
            result = prod3
            print i, j, result
        if prod4 > result:
            result = prod4
            print i, j, result
        if prod5 > result:
            result = prod5
            print i, j, result
        if prod6 > result:
            result = prod6
            print i, j, result
        if prod7 > result:
            result = prod7
            print i, j, result
        if prod8 > result:
            result = prod8
            print i, j, result

print result

