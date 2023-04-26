"""
Write a program that prints a string reversed using a loop.

All the characters must be on the same line in reverse order.
"""

word = input()

for char in word[::-1]:
    print(char, end="")
