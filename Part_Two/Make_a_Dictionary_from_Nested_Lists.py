"""
Write a program that creates a dictionary from the values
contained in nested lists.
Each nested list has this format [value1, value2].
value1 should be the key in the dictionary and value2 should be its
corresponding value.
If there are no nested lists, print an empty dictionary.
"""
my_list = [["a", 1], ["b", 2], ["c", 3], ["d", 4]]
my_dict = {}

for element in my_list:
    key = element[0]
    value = element[1]
    my_dict[key] = value

print(my_dict)
