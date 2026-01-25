"""
Stats model:
=============
Basic statistic functions.
"""


def average(numbers):
    """
    Calculate the average of a numbers list.
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_max(numbers):
    """
    Find the biggest number.
    """
    if not numbers:
        return None
    return max(numbers)

def find_min(numbers):
    """
    Find the smallest number.
    """
    if not numbers:
        return None
    return min(numbers)

def median(numbers):
    """
    Find the median of the numbers.
    """
    if not numbers:
        return 0
    numbers.sort()
    return numbers[len(numbers) // 2]