""" Highest and Lowest - 7 Kyu Kata Fundamentals

DESCRIPTION:
In this little assignment you are given a string of space separated
numbers, and have to return the highest and lowest number.

EXAMPLE:
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"

NOTES:
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
"""


# My solution
def high_and_low(numbers: str) -> str:
    # Vars used for readability purposes, but they could be skipped.
    nums = numbers.split()
    maxi, mini = max(nums, key=int), min(nums, key=int)
    return f"{maxi} {mini}"
