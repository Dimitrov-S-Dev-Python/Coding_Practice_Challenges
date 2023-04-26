"""
Write a Python program that reads a text file and saves its content
line by line to a list called file_content.
The list should contain strings that represent each line of the text file.
The program should print the resulting list
"""
# file_path = "basic_file.txt"
# file_content = []
#
# with open(file_path, "r") as file:
#     for line in file:
#         file_content.append(line)
#
# print(file_content)

with open("basic_file.txt", "r") as file:
    content = file.readlines()

print(content)


