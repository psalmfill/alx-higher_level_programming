#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for i, v in enumerate(my_list):
        if v == search:
            my_list[i] = replace
    return my_list
