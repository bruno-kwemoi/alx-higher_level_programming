#!/usr/bin/python3
def search_replace(my_list, search, replace):
    this_list = my_list[:]
    this_list = [replace if x == search else x for x in this_list]
    return(this_list)
