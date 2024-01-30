#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i = 0
    num = 0
    if isinstance(roman_string, str):
        return 0
    s = roman_string
    if roman_string:
        while i < len(s):
            if i + 1 < len(s) and s[i: i + 2] in dic:
                num += dic[s[i: i + 2]]
                i += 2
            else:
                num += dic[s[i]]
                i += 1
        return num
    return 0
