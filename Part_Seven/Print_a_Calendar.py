"""
Write a program that prints the calendar of a given month in a given year.
The user should be able to specify the month and year.
The month must be an integer between 1 and 12.
The year must be a valid integer.
If the values entered by the user are not valid, a descriptive message
should be displayed.
For example, if month is 7 (July) and year is 2021, the output should be:

     July 2021
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31
"""
import  calendar

print("Welcome to Python Calendar")
year = int(input("Enter a year (with this format YYYY): "))
month = int(input("Enter a month (1- 12): "))
print(calendar.month(year, month))
