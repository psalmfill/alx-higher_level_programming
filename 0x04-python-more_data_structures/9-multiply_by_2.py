#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = dict()
    for i in a_dictionary.keys():
        new_dict.update({i: a_dictionary[i] * 2})
    return new_dict
