"""
Write a program that prints the string s without the character at index n.
If the index n is out of range, print the string s intact.
If the string s is empty, print the string s intact.
"""
s = input()
n = int(input())

if n in range(len(s)):
    new_s = s[:n] + s[n + 1:]
    print(new_s)
else:
    print(s)
