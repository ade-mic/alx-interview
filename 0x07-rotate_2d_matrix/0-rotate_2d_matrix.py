#!/usr/bin/python3
"""
For the “0. Rotate 2D Matrix” project,
we are tasked with implementing an in-place
algorithm to rotate an n x n 2D matrix
by 90 degrees clockwise.
This challenge requires a good understanding
of matrix manipulation and in-place operations
in Python. Below are the key concepts and
resources that you need to grasp in order
to successfully complete this project.
"""
def rotate_2d_matrix(matrix):
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
