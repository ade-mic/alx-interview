#!/usr/bin/python3
"""
    In a text file, there is a single character H.
    Your text editor can execute only two operations in this file:
    Copy All and Paste. Given a number n,
    write a method that calculates the fewest number
    of operations needed to result in exactly n H characters in the file.

    Prototype: def minOperations(n)
    Returns an integer
    If n is impossible to achieve, return 0
"""


def minOperations(n):
    """
    In a text file, there is a single character H.
    Your text editor can execute only two operations in this file:
    Copy All and Paste. Given a number n,
    write a method that calculates the fewest number
    of operations needed to result in exactly n H characters in the file.

    Prototype: def minOperations(n)
    Returns an integer
    If n is impossible to achieve, return 0
    """
    if n <= 1:
        return 0

    operations = 0
    # Start checking for factors from 2 to n
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            # Add the factor
            operations += i
            # Reduce n
            n //= i
    if n > 1:
        # If n is still greater than 1, it is prime
        operations += n

    return operations
