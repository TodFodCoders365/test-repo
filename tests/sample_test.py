
def add(a: int, b: int) -> int:
    return a + b

def average(nums: list[int]) -> float:
    if not nums:
        raise ZeroDivisionError("Cannot compute average of empty list")
    return sum(nums) / len(nums)

def first_item_plus_one(lst: list[int]) -> int:
    if not lst:
        raise IndexError("List is empty")
    return lst[0] + 1

def safe_divide(a: int, b: int) -> int:
    return a // b
