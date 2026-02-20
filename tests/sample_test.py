import pytest


def add(a, b):
    """Return the sum of a and b as an integer."""
    return int(a) + int(b)


def average(numbers):
    """Return the arithmetic mean of a list of numbers.
    Raises ZeroDivisionError if the list is empty."""
    if not numbers:
        raise ZeroDivisionError("Cannot compute average of empty list")
    return sum(numbers) / len(numbers)


def first_item_plus_one(lst):
    """Return the first item of the list incremented by one.
    Raises IndexError if the list is empty."""
    if not lst:
        raise IndexError("List is empty")
    return lst[0] + 1


def safe_divide(a, b):
    """Divide a by b safely.
    Raises ZeroDivisionError if b is zero."""
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b
