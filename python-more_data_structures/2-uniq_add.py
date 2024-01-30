#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    nl = list(dict.fromkeys(my_list))
    for i in nl:
        sum += i
    return sum
