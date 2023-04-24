# Write a Python program that prints the string s without
# the characters located at even indices.
# If the string is empty or only has one character, print it without any changes.

s = input()

if len(s) <= 1:
    print(s)
else:
    new_s = ""
    for i in range(len(s)):
        if i % 2 != 0:
            new_s += s[i]
    print(new_s)
