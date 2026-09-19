#!/usr/bin/python3
"""
Module that calculates the fewest number of operations
needed to result in exactly n H characters in a file.
"""
def minOperations(n):
    """
    This Function calculates the fewest number of operations
    needed to result in exactly n H characters in a file.
    """
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
    