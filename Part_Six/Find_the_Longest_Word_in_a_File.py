"""
Write a program that finds and prints the longest word in a text file.
For this challenge, you may assume that the file only contains one word per line.
"""

with open("words.txt", "r") as file:
    content = file.readlines()

words = [x.strip("\n") for x in content]
max_length = sorted(words, key=lambda x: len(x),reverse=True)
print(max_length[0])
