#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    myKeys = list(a_dictionary.keys())
    myKeys.sort()
    sorted_dict = {i: a_dictionary[i] for i in myKeys}
    for i in sorted_dict.keys():
        print("{}: {}".format(i, sorted_dict[i]))
a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)
