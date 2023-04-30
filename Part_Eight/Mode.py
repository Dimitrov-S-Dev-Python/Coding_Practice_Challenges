"""
Write a function called mode. This function accepts a list of numbers
and returns the most frequent number in the list of numbers.
You can assume that the mode will be unique.
mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4])  # 4
"""

def mode(lst):
    my_dict = {}

    for number in lst:
        if number not in my_dict.keys():
            my_dict[number] = 0
        my_dict[number] += 1

    sorted_dict = sorted(my_dict.items(), key=lambda x: x[1])
    return sorted_dict[-1][0]
#
#
print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]))
