"""
Write a program that finds the sum of a list (or tuple) of numbers recursively.
Print the total sum.
If the list (or tuple) is empty, print 0.
"""
def find_sum(s):
    if not s:
        return 0
    else:
        return s[0] + find_sum(s[1:])

my_list = [1, 2, 3, 4]
print(find_sum(my_list))



