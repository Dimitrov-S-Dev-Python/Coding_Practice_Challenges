"""
Write a program that calculates and prints the sum of the digits of a positive
integer num.
The program must find the sum recursively.
If the integer has only one digit, print the integer as the total sum.
"""
def sum_of_digits(number):
    if number == 0:
        return 0
    else:
        return number % 10  + sum_of_digits(number // 10)

print(sum_of_digits(10))
