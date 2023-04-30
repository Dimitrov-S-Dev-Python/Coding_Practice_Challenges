"""
Write a function called repeat, which accepts a string and a number and
returns a new string with the string passed to the function repeated the
number amount of times. Do not use the built-in repeat method!
repeat('*', 3) # '***'
repeat('abc', 2) # 'abcabc'
repeat('abc', 0) # ''
"""

def repeat(string, num):
    if num == 0:
        return " "
    i = 0
    new_str = ""
    while i < num:
        new_str += string
        i += 1
    return new_str

print(repeat("abc", 0))
