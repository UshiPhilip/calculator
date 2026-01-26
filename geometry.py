from constants import PI
"""
Geometry functions
"""

def circle_area(radius):
    """
    Return a circle area.
    """
    return PI * (radius**2)

def rectangle_area(width, height):
    """
    Return a rectangle area.
    """
    return width * height

def triangle_area(base, height):
    """
    Return a triangle area.
    """
    return (base * height) / 2