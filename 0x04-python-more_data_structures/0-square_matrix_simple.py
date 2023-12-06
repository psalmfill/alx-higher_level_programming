#!/usr/bin/python3

def processMatrix(matrix=[]):
    if type(matrix) is not list:
        return matrix
    return [i**2 for i in matrix]


def square_matrix_simple(matrix=[]):
    newMatrix = []
    for i in matrix:
        newMatrix.append(processMatrix(i))
    return newMatrix
