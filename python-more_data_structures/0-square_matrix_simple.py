#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nmx = []
    for i in range(len(matrix)):
        nmx.append([])
        for j in range(len(matrix[i])):
            nmx[i].append(matrix[i][j] ** 2)
    return nmx
