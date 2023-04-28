"""
Write a program that creates and prints a frequency dictionary of the words
found in a text file.
The keys of the dictionary should be the words in the file.
The values should be their frequencies.
You may assume that each line of the file only contains one word.
"""

with open("words.txt", "r") as file:
    content = file.readlines()

words = [word.strip("\n") for word in content]
words_dict = {word:words.count(word) for word in words}
print(words_dict)
