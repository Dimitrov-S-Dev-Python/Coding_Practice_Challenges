"""
Write a Python program that prints the second-largest value in a list.
If the list is empty or only has one element, print None.
"""

list_items = [1, 2, 3, 4]

if len(list_items) > 1:
    list_items.sort()
    print(list_items[-2])
else:
    print("None")
