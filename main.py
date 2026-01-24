from operations import add, subtract, multiply, divide
from advanced import power, square_root
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

    else:
        print("Invalid selection...")