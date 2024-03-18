#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers"""
    if matrix == [[]]:
        print()
    for row in matrix:
        for i in range(len(row)):
            if i == len(row) - 1:
                print("{}".format(row[i]))
            else:
                print("{} ".format(row[i]), end=' ')
