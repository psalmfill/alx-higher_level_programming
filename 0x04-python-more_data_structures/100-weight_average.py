#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    return sum([n * b for n, b in my_list]) / sum(b for n, b in my_list)
