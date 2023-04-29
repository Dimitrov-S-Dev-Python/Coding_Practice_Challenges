"""
Write a function called list_check, which accepts a list and returns True
if each value in the list is a list.
Otherwise, the function should return False.
"""

def list_check(collection):
    return all(type(l) == list for l in collection)

print(list_check([[],[1],[2,3]]))