"""
Write a program that writes the elements of a list to the file
denoted by the variable file.
Each element should be written on a separate line.
The file should be new or its existing content must be replaced by this new content.
Expected Output:
If this is the list:

[1, 2, 3, 4, 5]
After running the program, the content of the file should be:

1
2
3
4
5
"""

content = [1, 2, 3, 4, 5]

with open("new_file.txt", "a") as file:
    for element in content:
        file.write(str(element) + "\n")