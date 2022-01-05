#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    el = [None] * len(matrix)
    for i in range(0, len(matrix)):
        el[i] = list(map(lambda x: x ** 2, matrix[i]))
    return el
