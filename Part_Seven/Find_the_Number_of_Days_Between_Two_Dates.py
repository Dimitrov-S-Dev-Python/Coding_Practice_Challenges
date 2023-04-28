"""
Write a Python program that calculates and prints the number of days between to given dates.
The user should be able to enter the two dates (one per line) with this format Year Month Day.
The year must be formatted with four digits. Example: 2021
The month must be an integer between 1 and 12 (with no leading zeros).
The day must be an integer between 1 and 31 (with no leading zeros).
The first date must be previous or equal to the second date.
If the dates are equal (there are 0 days between them), display the message:
"The dates are equal".
If there is only one day between the two dates, display the message:
"There is 1 day between these dates."
If the first date is later than the second date, print the message:
"Please enter valid dates"
"""

import  datetime

date1 = input("Enter first date: ")
date2 = input("Enter the second date: ")

date1_list = date1.split()
year1 = int(date1_list[0])
month1 = int(date1_list[1])
day1 = int(date1_list[2])

date1_obj = datetime.date(year1, month1, day1)

date2_list = date2.split()
year2 = int(date2_list[0])
month2 = int(date2_list[1])
day2 = int(date2_list[2])

date2_obj = datetime.date(year2, month2, day2)

if date2_obj < date1_obj:
    print("Please enter a valid dates.")
else:
    diff = (date2_obj - date1_obj).days

    if diff == 0:
        print("The dates are equal.")
    else:
        print(f"There are {diff} days between dates.")