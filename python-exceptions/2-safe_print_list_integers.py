#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    k = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            i += 1
        except (ValueError, TypeError):
            i += 1
            k += 1
            continue
    print()
    return i - k
