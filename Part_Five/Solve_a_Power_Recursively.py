"""
Write a program that find the value of a raised to the power b recursively.
The operation is a**b in Python, where "a" is the base and b is the exponent.
If the value of b is 0, the result is automatically 1
because every number raised to the power 0 is 1.
"""

def power_calculate(a, b):
    if b == 1:
        return a
    else:
        return a * power_calculate(a, b-1)

print(power_calculate(5, 2))
