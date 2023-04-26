"""
Write a program that prints Floyd's Triangle with n number of rows.

The value of n should be entered by the user. You may assume that
it is a positive integer.
Floyd's Triangle is made with consecutive numbers that
fill the rows with the triangle (as shown below).
If n is equal to 3:

1
2 3
4 5 6
"""

n = int(input())
count = 0

for row in range(1, n + 1):
    for col in range(0, row):
        count += 1
        print(count, end=" ")

    print()