"""
Write a function called sum_floats. This function should accept a variable
number of arguments. The function should return the sum of all the parameters
that are floats. If there are no floats the function should return 0

"""
def sum_floats(*args):
    return sum(arg for arg in args if type(arg) == float) or 0

print(sum_floats(1.5, 2.4, 'awesome', [], 1))
