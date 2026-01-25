"""
Text calculation
"""

from operations import add, subtract, multiply, divide
from advanced import power, square_root

# Testing basic calculations
assert add(3, 5) == 8, "Addition test failed."
assert subtract(5, 2) == 3, "Subtract test failed."
assert multiply(3, 5) == 15, "Multiply test failed."
assert divide(10, 2) == 5, "Dividing test failed."

# Testing advanced calculations
assert power(2, 3) == 8, "Power test failed."
assert square_root(16) == 4, "Square root test failed."

print("All the tests passed successfully!")