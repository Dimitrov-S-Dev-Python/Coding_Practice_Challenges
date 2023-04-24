# Write a Python program that check if a string only contains numbers.
# If it does, print True. Else, print False.

s = input()
is_digit = True
for i in s:
    if i.isalpha():
        is_digit = False
        break

print(is_digit)
