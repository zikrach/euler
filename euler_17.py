# -*- coding: utf-8 -*-
"""solve 17"""

dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 0: "zero",
        11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen",
        15:"fifteen", 16:"sixteen", 17: "seventeen", 
        18: "eighteen", 19: "nineteen", 20: "twenty", 
        30: "thirty", 40: "forty", 50: "fifty", 10:"ten",
        60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety",
        100:"hundred", 1000:"one thousand"}

def words(number):
    string = str(number)
    if len(string) == 1:
        result = dict[number]
    if len(string) == 2:
        if number < 20:
            result =  dict[number]
        elif string[1] == '0':
            result = dict[number]
        else:
            result = dict[int(string[0]) * 10] + '-' + dict[int(string[1])]
    if len(string) == 3:
        if string[1] == '0':
            if int(string[1:3]) == 0:
                result = dict[int(string[0])] + ' ' + dict[100]
            else:
                result = dict[int(string[0])] + ' ' + dict[100] + ' and ' + \
                    dict[int(string[1:3])] 
        elif int(string[1:]) < 20:
            result = dict[int(string[0])] + ' ' + dict[100] + ' and ' + \
                    dict[int(string[1:])] 
        elif int(string[2]) == 0:
            result = dict[int(string[0])] + ' ' + dict[100] + ' and ' + \
                    dict[int(string[1]) * 10] 
        else:
            result = dict[int(string[0])] + ' ' + dict[100] + ' and ' + \
                    dict[int(string[1]) * 10] + '-' + dict[int(string[2])]
    if len(string) == 4:
        result = dict[number]
    return (result, result.replace(' ','').replace('-',''))

result = 0

print words(200), len(words(100)[1])

for i in range(1, 1001):
    print i, words(i)
    result += len(words(i)[1])

print result
