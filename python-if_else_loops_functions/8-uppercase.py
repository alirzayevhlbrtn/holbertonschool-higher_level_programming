#!/usr/bin/python3
def uppercase(str):
    ustr = ""
    for letter in str:
        if ord(letter) > 96 and ord(letter) < 123:
            ustr += chr(ord(letter) - 32)
        else:
            ustr += letter
    return ustr
