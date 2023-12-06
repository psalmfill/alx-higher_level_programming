#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = dict()
    for key, v in a_dictionary.items():
        if v != value:
            new_dict.setdefault(key, v)
    return new_dict
