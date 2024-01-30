#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nlist = []
    for i in my_list:
        if i == search:
            nlist.append(replace)
        else:
            nlist.append(i)
    return nlist
