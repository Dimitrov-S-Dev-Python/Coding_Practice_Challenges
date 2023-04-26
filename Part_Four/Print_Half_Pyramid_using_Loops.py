"""
Write a program that prints a pyramid pattern made with asterisks.
The number of rows should be determined by the value of the variable n.
This value will be entered by the user.
You may assume that the value of n is a positive integer.
If the value of n is 5, this is the expected output:

        *
      * *
    * * *
  * * * *
* * * * *
"""

number_rows = int(input())

k = (2 * number_rows) - 2

for row in range(number_rows):
    for space in range(k):
        print(" ", end="")

    k = k - 2
    for asterisk in range(0, row + 1):
        print("*", end=" ")
    print()
