#!/usr/bin/python3
"""
Menasiz xetalar toplusu v2
"""


def text_indentation(text):
    """
    Function of print
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    banned = [".", "?", ":"]

    for i in range(len(text)):
        if text[i] in banned:
            print(text[i], end="")
            print()
        elif text[i] == " ":
            for j in (i, 0, -1):
                if text[j] == " ":
                    continue
                elif text[j] in bannedd:
                    break
                else:
                    print(text[i], end="")
                    break
        else:
            print(text[i], end="")
