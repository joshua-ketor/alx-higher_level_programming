#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    """ compute the square value of all integers of a matrix using map """
    new_matrix = []
    for row in matrix:
        new_matrix.append(list(map(lambda x: x**2, row)))
    return new_matrix
