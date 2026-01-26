"""
colors model:
================
Terminal output colors.
"""

# ANSI colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def print_success(message):
    """
    Print a green message.
    """
    print(f"{GREEN}{message}{RESET}")

def print_error(message):
    """
    Print a red message.
    """
    print(f"{RED}{message}{RESET}")

def print_result(message):
    """
    Print a blue message.
    """
    print(f"{BLUE}{message}{RESET}")
