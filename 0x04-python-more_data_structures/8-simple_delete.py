#!/usr/bin/

def simple_delete(a_dictionary, key=""):
    if key and key in a_dictionary.keys():
        a_dictionary.pop(key)
    return a_dictionary
