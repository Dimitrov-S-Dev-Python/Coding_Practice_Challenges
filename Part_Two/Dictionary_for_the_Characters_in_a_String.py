"""
Write a program that creates and displays a dictionary that maps
each letter in a string to how many times the character occurs
in the string (its frequency).
The dictionary should only include the characters in the string.
The test should be case-insensitive ("A" should be counted as "a").
The keys in the dictionary should be lowercase letters.
Only include letters in the dictionary.
"""

my_string = "Hello, World"
result = {}

for element in my_string.lower():
    if element.isalpha():
        if element not in result.keys():
            result[element] = 0
        result[element] += 1

print(result)
