""" Persistent Bugger - 6 Kyu Kata Fundamentals

DESCRIPTION:
Write a function, persistence, that takes in a positive parameter num and returns 
its multiplicative persistence, which is the number of times you must multiply 
the digits in num until you reach a single digit.

EXAMPLE (Input --> Output):

39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number)
"""

# My solution
from math import prod


def persistence(n):
    if len(str(n)) < 2:
        return 0

    counter = 0
    while len(str(n)) > 1:
        result = prod([int(number) for number in str(n)])
        n = result
        counter += 1
    return counter
