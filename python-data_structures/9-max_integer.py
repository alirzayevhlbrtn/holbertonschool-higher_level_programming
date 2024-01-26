#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        mx = 0
        for v in my_list:
            if v > mx:
                mx = v
        return mx
    return None
