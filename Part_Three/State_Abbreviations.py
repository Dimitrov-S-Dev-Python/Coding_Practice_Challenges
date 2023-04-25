"""
Given two lists ["CA", "NJ", "RI"] and
["California", "New Jersey", "Rhode Island"]
create a dictionary that looks like this
{'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}.
Save it to a variable called answer.
"""

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

answer = dict(zip(list1, list2))
print(answer)
