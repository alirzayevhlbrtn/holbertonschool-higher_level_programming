#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    ndic = a_dictionary.copy()
    for i in ndic.keys():
        ndic[i] *= 2
    return ndic
