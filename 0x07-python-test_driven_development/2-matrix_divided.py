#!/usr/bin/python3
def matrix_divided(matrix, div):
    """"Divides all elements of a matrix.

    Args:
        matrix: The matrix
        div(int or float): The divisor

    Raises:
        TypeError: if matrix is a not list of lists of integers or floats,
                    or matrix not of the same size,
                    or div is not n integer or float.
        ZeroDivisionError: if div equal to 0

    Returns: new matrix.
    """
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix(list of lists)
                            of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix(list of lists)
                                of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_element = round(element / div, 2)
            new_row.append(new_element)
        new_matrix.append(new_row)
    return new_matrix
