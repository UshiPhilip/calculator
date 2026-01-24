"""
Advanced model:
================
Including advanced calculations: Power By, Square Root, Modulo
"""


def power(base, exponent):
    """
    Power by
    """
    return base ** exponent

def square_root(n):
    """
    Square root
    """
    if n < 0:
        return "Error: No root for a negative number!"
    return n ** 0.5

def modulo(a, b):
    """
    Remainder from division
    """
    return a % b