#!/usr/bin/python3
import sys
"""
factorial - Calculate the factorial of a given non-negative integer using recursion.
 @n: A non-negative integer for which to calculate the factorial.
 Returns: The factorial of the given number.
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
