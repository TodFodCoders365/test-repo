# src/sample.py

def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def average(numbers):
    """Return the average of a list of numbers.
    Raises ZeroDivisionError if the list is empty.
    """
    if not numbers:
        raise ZeroDivisionError("Cannot compute average of empty list")
    return sum(numbers) / len(numbers)


def first_item_plus_one(items):
    """Return the first item of a list plus one.
    Raises IndexError if the list is empty.
    """
    if not items:
        raise IndexError("List is empty")
    return items[0] + 1


def safe_divide(a, b):
    """Return integer division of a by b.
    Raises ZeroDivisionError if b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a // b
