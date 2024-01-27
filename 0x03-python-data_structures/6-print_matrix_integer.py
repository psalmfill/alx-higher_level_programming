#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for arr in matrix:
        for idx,i in enumerate(arr):
            print("{:d}".format(i), end="") if idx == len(arr) - 1 else print("{:d}".format(i), end=" ")
        print()
