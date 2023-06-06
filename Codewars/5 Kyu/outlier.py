"""Find The Parity Outlier - 5 Kyu Kata Fundamentals

DESCRIPTION:
You are given an array (which will have a length of at least 3, but could be 
very large) containing integers. The array is either entirely comprised of odd
integers or entirely comprised of even integers except for a single integer N. 
Write a method that takes the array as an argument and returns this "outlier" N.

EXAMPLE:
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
"""


# My solution
def find_outlier(integers: list[int]) -> int:
    """
    Declares an acumulator for each kind of number using a generator expression.
    The generator expression creates a sequence of 1's for each integer that
    matches the condition, then it sums all of them.
    Then compares both variables and find the outlier depending on the case.
    Vars are used for readability purposes, but they could be skipped.
    """
    n_odd: int = sum(1 for num in integers if num % 2 != 0)
    n_even: int = sum(1 for num in integers if num % 2 == 0)
    if n_odd > n_even:
        # this means the outlier must be an even integer.
        # filter() will find the desired integer, then it's converted to
        # a tuple in order to obtain the found value.
        # same case for the odd outlier.
        even_outlier: int = tuple(filter(lambda num: num % 2 == 0, integers))[0]
        return even_outlier
    else:
        odd_outlier: int = tuple(filter(lambda num: num % 2 != 0, integers))[0]
        return odd_outlier
