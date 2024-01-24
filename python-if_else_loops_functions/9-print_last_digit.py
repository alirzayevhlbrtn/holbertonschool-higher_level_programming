#!/usr/bib/python3
def print_last_digit(number):
    lastd = int(str(number)[-1:])
    print("{}".format(lastd), end="")
    return lastd
