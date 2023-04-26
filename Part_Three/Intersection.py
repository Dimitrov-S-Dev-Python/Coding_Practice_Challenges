"""
Write a function called intersection. This function should accept two lists
and return a list with the values that are in both input lists.
intersection([1,2,3], [2,3,4])    #[2,3]
intersection(['a','b','z'], ['x','y','z']) .  # ['z']
"""

def intersection(collection1, collection2):
    return [x for x in collection1 if x in collection2]

print(intersection([1,2,3], [2,3,4]))

# Set Solution
def intersection(list1, list2):
    return [val for val in set(list1) & set(list2)]