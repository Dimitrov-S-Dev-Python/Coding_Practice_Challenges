"""
Write a program that calculates the factorial of a given number n.
The value of n should be entered by the user.
The program must print the result and use a loop to calculate it.
"""

n = int(input())

factorial = 1

for number in range(2, n + 1):
        factorial *= number

print(factorial)
