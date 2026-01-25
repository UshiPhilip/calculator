"""
Text calculation
"""

from operations import add, subtract, multiply, divide
from advanced import power, square_root
from stats import average, find_max, find_min, median

# Testing basic calculations
assert add(3, 5) == 8, "Addition test failed."
assert subtract(5, 2) == 3, "Subtract test failed."
assert multiply(3, 5) == 15, "Multiply test failed."
assert divide(10, 2) == 5, "Dividing test failed."

# Testing advanced calculations
assert power(2, 3) == 8, "Power test failed."
assert square_root(16) == 4, "Square root test failed."

# Testing statistic functions
assert average([1,2,3,4,5]) == 3, "Average test failed."
assert find_max([1,2,3,4,5]) == 5, "Find maximum test failed."
assert find_min([1,2,3,4,5]) == 1, "Find minimum test failed."
assert median([1,2,3,4,5]) == 3, "Median test failed."

print("All the tests passed successfully!")