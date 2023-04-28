"""
Write a program that prints the last n lines of a text file in order.
The value of n should be provided by the user.
You may assume that n is a valid positive integer.
"""

with open("basic_file.txt", "r") as file:
    content = file.readlines()

lines = len(content)
user_input = int(input("Please enter a value for n: "))

if user_input > lines:
    user_input = input(f"Please enter a value las then {lines}")
else:
    for i in range(-user_input, 0):
        print(content[i].strip("\n"))
