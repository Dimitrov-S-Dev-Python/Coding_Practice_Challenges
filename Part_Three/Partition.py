"""
Write a function called partition. This function accepts a list and a callback
function (which you can assume returns True  or False  ).
"""
def is_even(num):
    return num % 2 == 0

def partition(lst, fn):
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]

partition([1,2,3,4], is_even) # [[2,4],[1,3]]
