"""
Write a program that prints a triangular pattern like the ones shown below.
If the value of n is 3:

*
* *
* * *
If the value of n is 5:

*
* *
* * *
* * * *
* * * * *
"""

n = int(input())

for num in range(1, n + 1):
    print("* " * num)
