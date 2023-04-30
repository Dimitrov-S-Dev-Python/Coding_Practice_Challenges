"""
Write a function called is_odd_string which returns true if sum of
each character's position in the alphabet is odd.
For example, "a" is in the first position, "b" is in the second position, and so on.
If the sum is even, return false.  NOTE: INDEXING STARTS AT 1.
A is position 1, NOT POSITION 0.
"""
import string
def is_odd_string(text):
    total = 0
    word = string.ascii_lowercase
    for char in text:
        index = word.index(char) + 1
        total += index
    if total % 2 != 0:
        return True
    return False

print(is_odd_string('aaaa'))
