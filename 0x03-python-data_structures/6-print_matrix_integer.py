#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        temp = len(matrix[i])
        for j in range(0, temp):
            if j == temp - 1:
                print("{}".format(matrix[i][j]), end="")
            else:
                print("{}".format(matrix[i][j]), end=" ")
        print()
