"""
Write a function called find_the_duplicate which accepts an array of numbers
containing a single duplicate. The function returns the number
which is a duplicate or None if there are no duplicates.
find_the_duplicate([1,2,1,4,3,12]) # 1
find_the_duplicate([6,1,9,5,3,4,9]) # 9
find_the_duplicate([2,1,3,4]) # None
"""

def find_the_duplicate(lst):
    duplicate = []
    for elem in lst:
        if elem in duplicate:
            return elem
        duplicate.append(elem)


print(find_the_duplicate([1,2,1,4,3,12]))

"""
def find_the_duplicate(lst):
    counter = {}
    for val in lst:
        if val not in counter:
            counter[val] = 0
       counter[val] += 1
    for value in counter.values():
        if value > 1:
            return int(value)
"""
