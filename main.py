from operations import add, subtract, multiply, divide
from advanced import power, square_root, factorial
from stats import average, find_max, find_min, median
from history import add_to_history, show_history, clear_history
from ui import get_number, show_menu

print("╔════════════════════════════╗")
print("║ Welcome To Our Calculator! ║")
print("║        Version 4.0         ║")
print("╚════════════════════════════╝")

while True:
    choice = show_menu()

    if choice == "0":
        print("Good bye")
        break

    if choice in ["1", "2", "3", "4", "5"]:
        num1 = get_number("Enter your first number: ")
        num2 = get_number("Enter your second number: ")\

        if choice == "1":
            result = add(num1, num2)
            print(f"Result: {result}.")
            add_to_history(f"{num1} + {num2} = {result}")

        elif choice == "2":
            result = subtract(num1, num2)
            print(f"Result: {result}.")
            add_to_history(f"{num1} + {num2} = {result}")

        elif choice == "3":
            result = multiply(num1, num2)
            print(f"Result: {result}.")
            add_to_history(f"{num1} + {num2} = {result}")

        elif choice == "4":
            result = divide(num1, num2)
            print(f"Result: {result}.")
            add_to_history(f"{num1} + {num2} = {result}")

        elif choice == "5":
            result = power(num1, num2)
            print(f"Result: {result}.")
            add_to_history(f"{num1} + {num2} = {result}")

    elif choice == "6":
        num = get_number("Enter a number: ")
        result = square_root(num)
        print(f"Result: {result}.")
        add_to_history(f"{num} ** 0.5 = {result}")

    elif choice == "7":
        num = get_number("Enter a number: ")
        result = factorial(num)
        print(f"Result: {result}")
        add_to_history(f"{num} != {result}")

    elif choice == "8":
        num = get_number("Enter a number list: ")
        result = average(num)
        print(f"Result: {result}")
        add_to_history(f"{num}'s average = {result}")

    elif choice == "9":
        num = get_number("Enter a numbers list: ")
        result = find_max(num)
        print(f"Result: {result}")
        add_to_history(f"{num}'s minimum = {result}")

    elif choice == "10":
        num = get_number("Enter a number list: ")
        result = find_min(num)
        print(f"Result: {result}")
        add_to_history(f"{num}'s maximum = {result}")

    elif choice == "11":
        num = get_number("Enter a number list: ")
        result = median(num)
        print(f"result: {result}")
        add_to_history(f"{num}'s median = {result}")

    elif choice == "12":
        show_history()

    elif choice == "13":
        clear_history()

    else:
        print("Invalid selection...")