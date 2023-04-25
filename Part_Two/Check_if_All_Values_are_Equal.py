"""
Write a Python program that checks if all values in a dictionary are equal.
If they are, print True. Else, print False.
If the dictionary is empty, print "Empty"
"""

my_dict = {"a":4, "b":4, "c":4}

num_unique_values = len(set(my_dict.values()))

if num_unique_values == 0:
    print("Empty")
elif num_unique_values == 1:
    print("True")
else:
    print("False")
