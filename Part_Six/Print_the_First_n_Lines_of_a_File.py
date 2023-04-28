"""
Write a program that reads a text file and prints the first n lines of the file.
The value of n should be entered by the user.
If the value of n is greater than the total number of lines in the file, print
"Please enter a value for n. The file has
"""


with open("basic_file.txt", "r") as file:
    content = file.readlines()

n = int(input("Enter a value for n: "))

if n > len(content):
    n = input(f"Enter a value for n. The file has {len(content)} lines.")
else:
    for i in range(n):
        print(content[i].strip("\n"))

