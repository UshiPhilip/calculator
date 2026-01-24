from operations import add, subtract, multiply, divide
from advanced import power, square_root, modulo

print("============================")
print(" Welcome to our calculator!")
print("============================")

print("\nBasic actions:")

result = add(3,5)
print(f"3 + 5 = {result}")

result = subtract(5,3)
print(f"5 - 3 = {result}")

result = multiply(3,5)
print(f"3 * 5 = {result}")

result = divide(5,3)
print(f"5 / 3 = {result}")

print("\nAdvance actions:")

result = power(2,3)
print(f"2 ** 3 = {result}")

result = square_root(4)
print(f"4 ** 0.5 = {result}")

result = modulo(5,2)
print(f"5 % 2 = {result}")