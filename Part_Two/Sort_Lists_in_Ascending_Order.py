"""
Write a program that sorts (in ascending order) the lists contained as values
in a dictionary.
The dictionary contains key-value pairs that match strings to lists.
You need to sort these lists.
The lists have to be mutated (changed).
"""
my_dict = {
	"a": [4, 3, 2],
	"b": [5, 3, 7],
	"c": [1, 9, 10],
	"d": [3, 4, 1]
}

for list_values in my_dict.values():
    list_values.sort()

print(my_dict)
