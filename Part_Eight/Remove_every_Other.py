"""
Write a function called remove_every_other that accepts a list and returns
a new list with every second value removed.
"""

def remove_every_other(collection):
    return [value for index, value in enumerate(collection) if index % 2 == 0]

print(remove_every_other([1, 2, 3, 4, 5]))
