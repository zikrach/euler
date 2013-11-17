# -*- coding: utf-8 -*-
"""solve 13"""


def terms(arg):
    yield arg
    while arg != 1:
        if arg % 2 == 0:
            arg = arg / 2
        else:
            arg = 3 * arg + 1
        yield arg

print list(terms(13)), len(list(terms(13)))

number = 13
lengh = 10

while number <= 1000000:
    if len(list(terms(number))) >= lengh:
        lengh = len(list(terms(number)))
        print number, lengh
    number += 1
