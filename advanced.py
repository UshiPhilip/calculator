"""
Advanced model:
================
Including advanced calculations: Power By, Square Root, Modulo
"""


def power(base, exponent):
    """
    Power by.
    """
    return base ** exponent

def square_root(n):
    """
    Square root.
    """
    if n < 0:
        return "Error: No root for a negative number!"
    return n ** 0.5

def modulo(a, b):
    """
    Remainder from division.
    """
    return a % b

def factorial(n):
    """
    Calculate a factorial for a number.
    """
    if n < 0:
        return "Error: There is no factorial to a negative number!"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result