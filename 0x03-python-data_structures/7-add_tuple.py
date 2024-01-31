#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # prepare the tuple
    new_tuple_a = (tuple_a[i] if i < len(tuple_a) else 0 for i in range(0,2) ) 
    new_tuple_b = (tuple_b[i] if i < len(tuple_b) else 0 for i in range(0,2) ) 
    return tuple(map(sum,zip(new_tuple_a, new_tuple_b)))