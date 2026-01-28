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
    print("8. Average")
    print("9. Find maximum")
    print("10. Find minimum")
    print("11. Median")
    print("12. Circle area")
    print("13. Rectangle area")
    print("14. Triangle area")
    print("15. Percentage")
    print("16. Currency converter")
    print("17. Converting from C° to F°")
    print("18. Shows constants")
    print("=== History ===")
    print("19. Show history")
    print("20. Clear history")
    print("0. Exit")
    return input("Chose an action: ")
