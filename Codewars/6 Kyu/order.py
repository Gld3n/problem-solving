""" Your order, please - 6 Kyu Kata Fundamentals

DESCRIPTION:
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
"""


# My solution
def order(sentence: str) -> str:
    if not sentence:
        return ""
    words_with_digits = [(word, check_int(word)) for word in sentence.split()]
    words_with_digits.sort(key=lambda x: x[1])
    sorted_words = [word[0] for word in words_with_digits]
    return " ".join(sorted_words)


def check_int(word):
    return [int(char) for char in word if char.isdigit()]
