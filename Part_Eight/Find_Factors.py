"""
Write a function called find_factors which accepts a number and returns a list
of all the numbers which are is divisible by starting from 1 and going up to the number.
find_factors(10) # [1,2,5,10 ]
find_factors(11) # [1,11]
find_factors(111) # [1,3,37,111 ]
find_factors(321421) # [1,293,1097,321421 ]
"""

def find_factors(number):
    factors = []
    for num in range(1, number + 1):
        if number % num == 0:
            factors.append(num)
    return factors

print(find_factors(111))