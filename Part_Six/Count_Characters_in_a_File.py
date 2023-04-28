"""
Write a program that counts the number of characters in a file.
Count all the characters in the file, including commas and quotes.
Do not count spaces and remove \n (new line) characters.
Expected Output:
If this is the content of the char.txt file:
Total Number of Characters: 339
"""

character_count = 0
with open("char.txt", "r") as file:
    for line in file:
        character_count += len(line.replace(" ", "").strip("\n"))

print(character_count)