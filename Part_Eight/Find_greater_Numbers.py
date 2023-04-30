"""
Write a function called find_greater_numbers which accepts a list
and returns the number of times a number is followed by a larger number across
the entire list.
find_greater_numbers([1,2,3]) # 3
find_greater_numbers([6,1,2,7]) # 4
find_greater_numbers([5,4,3,2,1]) # 0
find_greater_numbers([]) # 0
"""

def find_greater_numbers(lst):
    count = 0

    for index, value in enumerate(lst):
        for index2, value2 in enumerate(lst[index + 1:]):
            if value2 > value:
                count += 1
    return count

print(find_greater_numbers([6, 1, 2, 7]))
