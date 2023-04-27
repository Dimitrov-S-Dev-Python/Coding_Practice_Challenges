"""
Write a program that calculates and prints the nth Fibonacci number.
The value of n represents the position of the element in the sequence.
The initial value of n should be 0.
You may assume that the value of n is a non-negative integer.
The Fibonacci sequence is a series of numbers where the
next number is the result of adding the previous two numbers.
The sequence starts with 0 and 1.
"""

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(3))
