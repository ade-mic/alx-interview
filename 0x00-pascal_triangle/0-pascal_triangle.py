#!/usr/bin/python3
'''
a function of pascal triangle with n integer.It returns a list
of integers representing the Pascal's triangle of n
'''

def factorial(n):
    """
    Calculates the factorial of a non-negative integer n.

    Args:
        n (int): Non-negative integer.

    Returns:
        int: Factorial of n.
    """
    if n == 0:
        return 1
    else:
        # Recursive step: n! = n * (n-1)!
        return n * factorial(n - 1)

def pascal_triangle(n):
    """
    a function that returns a pascal tiangle of n

    Args
        n(integer): The integer to be calculated for a pascal triangle.

    Return:
        list: The of list of lists of integers representing the pascal triangle
        Returns an empty list if n <= 0
    """
    triangle = []
    # return empty list if n <= 0
    if n <= 0:
            return triangle
    for row in range(n):
        li = []
        for i in range(0, row):
            li.append(int(factorial(row) / (factorial(i) * (factorial(row - i)))))
        triangle.append(li + [1])
    return triangle
