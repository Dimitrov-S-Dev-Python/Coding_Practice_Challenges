"""
Write a program that prints a triangular pattern made with letters
(as shown below).
A
B B
C C C
The ASCII code points for uppercase letters start at 65 for "A"
"""
# n = int(input())
# count = 65
# for row in range(1, n + 1):
#     for col in range(0, row):
#         print(chr(count), end=" ")
#     count += 1
#     print()

n = int(input())

for row in range(0,n):
    print((chr(65 + row) + " ") * (row + 1))
