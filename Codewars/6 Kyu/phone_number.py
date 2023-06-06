""" Create Phone Number - 7 kyu Kata Fundamentals

DESCRIPTION:
Write a function that accepts an array of 10 integers (between 0 and 9), 
that returns a string of those numbers in the form of a phone number.

EXAMPLE:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.

Don't forget the space after the closing parentheses!
"""


# My solution
def create_phone_number(n: list[int]) -> str:
    # Convert each number in the list to a string and slice it.
    # Then join the sliced numbers in blocks to be formatted nicely.
    first = "".join([str(i) for i in n[0:3]])
    second = "".join([str(i) for i in n[3:6]])
    third = "".join([str(i) for i in n[6:10]])
    return f"({first}) {second}-{third}"
