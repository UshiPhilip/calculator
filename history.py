"""
History model:
===============
Keeps calculations history.
"""

# List to save history.
calculation_history = []

def add_to_history(expression, result):
    """
    Add a calculation to the history.
    """
    entry = f"{expression} = {result}"
    calculation_history.append(entry)

def show_history():
    """
    Shows history.
    """
    if not calculation_history:
        print("The history is empty.")
        return

    print("\n=== History ===")
    for i, entry in enumerate(calculation_history, 1):
        print(f"{i}. {entry}")

def clear_history():
    """
    Cleans the history.
    """
    calculation_history.clear()
    print("History deleted.")