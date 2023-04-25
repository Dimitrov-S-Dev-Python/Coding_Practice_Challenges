"""
Write a program that multiplies all the items in a list
by the value of the variable factor.
The program must print the list as the output.
The program should also allow multiplying the variable factor
by a string in case the list contains strings.
You may assume that the value of factor will be a positive integer.
"""

list_items = [3, 4, 5, "a"]
factor = int(input())
result = [x * factor for x in list_items]
print(result)
