"""
Write a program that prints the maximum sum of the values in a dictionary.
You may assume that all the values in the dictionary are either lists or tuples.
"""
my_dict = {
	"a": [1, 2, 3],
	"b": [4, 0, -4],
	"c": [3, 5, 9],
	"d": [45, 12, 100]
}
max_sum = None

for list_values in my_dict.values():
    curr_sum = sum(list_values)
    if max_sum is None:
        max_sum = curr_sum
    elif curr_sum > max_sum:
        max_sum = curr_sum

print(max_sum)
