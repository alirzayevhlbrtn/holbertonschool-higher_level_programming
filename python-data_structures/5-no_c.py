#!/usr/bin/python3
def no_c(my_string):
    n_str = ""
    for c in my_string:
        if c != "c" and c != "C":
            n_str += c
    return n_str
