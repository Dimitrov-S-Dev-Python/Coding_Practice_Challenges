"""
Write a function called same_frequency which accepts two numbers and returns
True if they contain the same frequency of digits. Otherwise, it returns False.
same_frequency(551122,221515) # True
same_frequency(321142,3212215) # False
same_frequency(1212, 2211) # True
"""


def same_frequency(num1, num2):
    d1 = {number: str(num1).count(number) for number in str(num1)}
    d2 = {number: str(num2).count(number) for number in str(num2)}

    for key, val in d1.items():
        if not key in d2.keys():
            return False
        elif d2[key] != d1[key]:
            return False
    return True


print(same_frequency(552211, 221155))
