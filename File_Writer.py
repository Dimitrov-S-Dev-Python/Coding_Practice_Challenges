# Create a program that asks the user to input values until CLOSE is the value
# and stores those values in a text file, each value in a separate line.

file = open("User_Data.txt", "a+")
while True:
    line = input("Write a value")
    if line == "CLOSE":
        file.close()
        break
    else:
        file.write(line + "\n")
