def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def average(numbers):
    """Return the arithmetic mean of a non-empty list of numbers.
    Raises ZeroDivisionError if the list is empty.
    """
    if not numbers:
        raise ZeroDivisionError("Cannot compute average of an empty list.")
    return sum(numbers) / len(numbers)


def first_item_plus_one(lst):
    """Return the first item of the list incremented by one.
    Raises IndexError if the list is empty.
    """
    if not lst:
        raise IndexError("List is empty.")
    return lst[0] + 1


def safe_divide(a, b):
    """Return the integer division of a by b.
    Raises ZeroDivisionError if b is zero.
    """
    return a // b
