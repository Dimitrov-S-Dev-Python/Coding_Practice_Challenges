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
max_sum = 0

for v in my_dict.values():
    curr_sum = sum(v)
    if curr_sum > max_sum:
        max_sum = curr_sum

print(max_sum)
