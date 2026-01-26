"""
Operator model:
===============
Including basic calculations: Addition, Subtract, Multiply, Dividing
"""
from GitKreken.calculator.colors import print_error


def add(a, b):
    """Adding two numbers"""
    return a + b

def subtract(a, b):
    """Substructure two numbers"""
    return a - b

def multiply(a, b):
    """
    Multiply two numbers
    """
    return a * b

def divide(a, b):
    """
    Dividing two numbers
    """
    if b == 0:
        print_error("Error: you can NOT dividing by zero!")
        return None
    return a / b