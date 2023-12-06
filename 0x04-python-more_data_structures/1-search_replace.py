#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i, v in enumerate(my_list):
        print(i)
        if v == search:
            new_list.append(replace)
        else:
            new_list.append(v)
    return new_list
