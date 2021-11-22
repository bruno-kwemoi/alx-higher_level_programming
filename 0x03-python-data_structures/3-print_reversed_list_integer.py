#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new_list = my_list[::-1]
    n = len(new_list)
    for i in range(0, n):
        print("{}".format(new_list[i]))
