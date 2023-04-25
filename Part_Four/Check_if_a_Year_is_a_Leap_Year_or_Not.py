"""
This is how you can determine if a year is a leap year or not:
if (year is not divisible by 4) then (it is a common year).
else if (year is not divisible by 100) then (it is a leap year)
else if (year is not divisible by 400) then (it is a common year)
else (it is a leap year)
"""

year = 1912

if year % 4 == 0:
    if year % 100 == 0:

        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")

else:
    print(f"{year} is not a leap year")
