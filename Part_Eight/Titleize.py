"""
Write a function called titleize which accepts a string of words and returns
a new string with the first letter of every word in the string capitalized.
titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"
"""

def titleize(string):
    string_list = string.split()
    title_list = [x[0].upper() + x[1:] for x in string_list]
    return " ".join(title_list)

print(titleize("oNLy cAPITALIZe fIRSt"))