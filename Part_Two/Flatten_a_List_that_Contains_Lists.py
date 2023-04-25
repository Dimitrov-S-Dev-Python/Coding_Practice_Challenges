"""
Write a Python program that prints a "flattened" version of a list
that contains nested lists.
"""

list_items = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = []
for elem in list_items:
    for item in elem:
        result.append(item)
print(result)
