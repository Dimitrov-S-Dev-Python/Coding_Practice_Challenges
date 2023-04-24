"""
Write a Python program to convert a string s to lowercase, sort the characters
of each word in alphabetical order, and print the resulting string.
You may assume that the string only contains letters
and spaces to separate the words.
Spaces should be preserved in the final string.
"""
word_list = input().lower().split()
s_sorted = []

for word in word_list:
    sort_s = "".join(sorted(word))
    s_sorted.append(sort_s)
print(" ".join(s_sorted))
