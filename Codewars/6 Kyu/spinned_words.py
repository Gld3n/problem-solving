"""Stop gninnipS My sdroW! - 6 kyu Kata Fundamentals

DESCRIPTION:
Write a function that takes in a string of one or more words, and
returns the same string, but with all five or more letter words 
reversed (Just like the name of this Kata). Strings passed in will 
consist of only letters and spaces. Spaces will be included only 
when more than one word is present.

EXAMPLE:
spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"
"""


# My solution
def spin_words(sentence: str) -> str:
    # generator expression with a ternary operator
    string = " ".join(
        word[::-1] if len(word) > 4 else word for word in sentence.split()
    )
    return string
