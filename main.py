from Learning_Python.Functions.part_0.q3 import return_to_base
from operations import add, subtract, multiply, divide
from advanced import power, square_root, factorial
from stats import average, find_max, find_min, median
from ui import get_number, show_menu

print("============================")
print(" Welcome To Our Calculator!")
print("============================")

while True:
    choice = show_menu()

    if choice == "0":
        print("Good bye")
        break

    if choice in ["1", "2", "3", "4", "5"]:
        num1 = get_number("Enter your first number: ")
        num2 = get_number("Enter your second number: ")\

        if choice == "1":
            print(f"Result: {add(num1, num2)}.")
        elif choice == "2":
            print(f"Result: {subtract(num1, num2)}.")
        elif choice == "3":
            print(f"Result: {multiply(num1, num2)}.")
        elif choice == "4":
            print(f"Result: {divide(num1, num2)}.")
        elif choice == "5":
            print(f"Result: {power(num1, num2)}.")
    elif choice == "6":
        num = get_number("Enter a number: ")
        print(f"Result: {square_root(num)}.")

    elif choice == "7":
        num = get_number("Enter a number: ")
        print(f"Result: {factorial(num)}")

    elif choice == "8":
        num = get_number("Enter a number list: ")
        print(f"Result: {average(num)}")

    elif choice == "9":
        num = get_number("Enter a numbers list: ")
        print(f"Result: {find_max(num)}")

    elif choice == "10":
        num = get_number("Enter a number list: ")
        print(f"Result: {find_min(num)}")

    elif choice == "11":
        num = get_number("Enter a number list: ")
        print(f"result: {median(num)}")

    else:
        print("Invalid selection...")