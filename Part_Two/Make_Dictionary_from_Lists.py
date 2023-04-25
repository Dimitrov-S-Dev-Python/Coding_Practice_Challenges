"""
Write a program that creates and print a dictionary that maps
each element in a list to its corresponding frequency
(how many times it occurs in the list).
The test should be case-sensitive. Therefore, "A" should not be considered
the same element as "a"
"""

list_items = ["a", "a", "b", "c", "a", "b"]
result = {k: list_items.count(k) for k in list_items}
print(result)
