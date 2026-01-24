"""
Operator model:
===============
Including basic calculations: Addition, Subtract, Multiply, Dividing
"""

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
        return "Error: you can NOT dividing by zero!"
    return a / b