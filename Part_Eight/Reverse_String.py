"""
Write a function called reverse_string which accepts a string and returns a
new string with all the characters reversed.
reverse_string('awesome') # 'emosewa'
reverse_string('Colt') # 'tloC'
reverse_string('Elie') # 'eilE'
"""

def reverse_string(text):
    return text[::-1]

print(reverse_string("awesome"))
