"""
Write a program that checks if a number is prime or not.
If the number is prime, it should print "Prime".
If the number is not prime, it should print "Not prime".
A prime number is only divisible by 1 and by itself. It is not the
product of two smaller natural numbers.
"""

number = int(input())
is_prime = True

if number == 1:
    is_prime = False
else:
    for num in range(2, number):
        if number % num == 0:
            is_prime = False
            break

if is_prime:
    print("Prime")
else:
    print("Not Prime")
