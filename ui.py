"""
Ui model:
=========
Including functions to the user interface
"""

def get_number(prompt):
    """
    Catches a number from the user
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a number!")

def show_menu():
    """
    Shows the menu
    """
    print("\n=== MENU ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Root")
    print("7. Factorial")
    print("0. Exit")
    return input("Chose an action: ")
