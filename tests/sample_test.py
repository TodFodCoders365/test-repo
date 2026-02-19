# src/sample.py

def add(a, b):
    """
    Return the sum of a and b as a numeric value.
    """
    return a + b


def average(nums):
    """
    Return the arithmetic mean of a non-empty sequence of numbers.
    Raises ZeroDivisionError if the sequence is empty.
    """
    if not nums:
        raise ZeroDivisionError("average() of empty sequence")
    return sum(nums) / len(nums)


def first_item_plus_one(lst):
    """
    Return the first item of a list incremented by one.
    Raises IndexError if the list is empty.
    """
    if not lst:
        raise IndexError("first_item_plus_one() on empty list")
    return lst[0] + 1


def safe_divide(a, b):
    """
    Perform integer division of a by b.
    Raises ZeroDivisionError if b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a // b
