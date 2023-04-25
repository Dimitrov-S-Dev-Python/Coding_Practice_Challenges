"""
Write a Python program that prints the largest value in a dictionary.
If the dictionary is empty, print None.
You may assume that the values are numeric
"""

my_dict = {"a":4, "b":3, "c":7}

if my_dict:
    max_value = max(my_dict.values())
    print(max_value)
else:
    print("None")
