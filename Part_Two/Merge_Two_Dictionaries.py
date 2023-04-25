"""
Write a Python program that merges two dictionaries
and prints the resulting dictionary.
Notice that the key-value pairs that share the same key on both dictionaries
are not repeated. They are updated with the value of the second dictionary.
"""
my_dict1 = {"a": 1, "b": 2, "c": 3}
my_dict2 = {"c": 4, "d": 6, "e": 8}

result = my_dict1 | my_dict2
print(result)
