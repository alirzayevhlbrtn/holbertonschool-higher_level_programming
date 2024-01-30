#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nl = []
    for i in range(list_length):
        try:
            nl.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            nl.append(0)
            print("division by 0")
        except (ValueError, TypeError):
            nl.append(0)
            print("wrong type")
        except IndexError:
            nl.append(0)
            print("out of range")
            break
    return nl
