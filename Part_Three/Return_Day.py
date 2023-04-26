"""
Write a function called return_day. this function takes in one parameter
(a number from 1-7) and returns the day of the week (1 is Sunday, 2 is Monday,
3 is Tuesday etc.). If the number is less than 1 or greater than 7,
the function should return None
"""
'''
return_day(1) # "Sunday"
return_day(2) # "Monday"
return_day(3) # "Tuesday"
return_day(4) # "Wednesday"
return_day(5) # "Thursday"
return_day(6) # "Friday"
return_day(7) # "Saturday"
return_day(41) # None
'''

def return_day(num):
    days_dict = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    if num in days_dict.keys():
        return days_dict[num]


print(return_day(25))