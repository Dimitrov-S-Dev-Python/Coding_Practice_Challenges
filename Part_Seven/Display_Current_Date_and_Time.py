"""
Write a program that displays the current date and time.
The program should print Current Date and Time: on the previous line.
The date should be formatted as YYYY-MM-DD
The time should be formatted as HH:MM:SS
"""

from datetime import datetime

print("Current date and time:")
today = datetime.now()
print(today.strftime("%Y-%m-%d %H:%M:%S"))