#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    my_dict = {}
    my_dict.update((x, y * 2) for x, y in a_dictionary.items())
    return(my_dict)
