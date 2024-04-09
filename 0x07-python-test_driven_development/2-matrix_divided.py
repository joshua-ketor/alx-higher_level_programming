#!/usr/bin/python3
"""Module for the divide matrix function"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix
    Args:
        matrix (list): The matrix (list of lists)
        div (int, float): The divisor for each element in the matrix

    Returns:
        A new matrix with elements rounded to 2 decimal places

    Raises:
        TypeError: if the matrix elements are not either integer or float
        TypeError: if each row of the matrix is not of the same size
        TypeError: if div is not a number
        ZeroDivisionError: if div is equal to 0
    """
    new_matrix = []
    if (type(matrix) is not list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if len(matrix) == 0:
        return new_matrix
    if type(matrix[0]) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    rlen = len(matrix[0])
    row = 0
    for i in matrix:
        if type(i) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
        new_matrix.append([])
        for elem in i:
            if len(i) != rlen:
                raise TypeError(
                    "Each row of the matrix must have the same size"
                )
            if type(elem) not in [int, float]:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )
            new_matrix[row].append(round((elem / div), 2))

        row += 1
    return new_matrix
