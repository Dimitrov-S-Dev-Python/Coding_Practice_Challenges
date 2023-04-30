"""
Write a function called three_odd_numbers, which accepts a list of numbers
and returns True  if any three consecutive numbers sum to an odd number.
three_odd_numbers([1,2,3,4,5]) # True
three_odd_numbers([0,-2,4,1,9,12,4,1,0]) # True
three_odd_numbers([5,2,1]) # False
three_odd_numbers([1,2,3,3,2]) # False
"""


def three_odd_numbers(lst):
    i = 0
    while i < (len(lst) - 2):
        total = 0
        j = i
        while j <= i + 2:
            total += lst[j]
            j += 1

        if (j - i) % 3 == 0 and total % 2 != 0:
            return True

        i += 1
    return False

print(three_odd_numbers([1,2,3,3,2]))
