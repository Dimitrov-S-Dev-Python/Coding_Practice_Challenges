"""
Write a program that converts seconds to minutes and hours.
Present the minutes as an integer and the hours as a decimal value.
"""
seconds = 7200
minutes = seconds // 60
hours = minutes / 60
print(f"{seconds}, seconds is equivalent to: ")
print(f"{minutes} minutes")
print(f"{hours} hours")