import string, os

# file_extension = string.ascii_lowercase
#
# for letter in file_extension:
#     file = letter + ".txt"
#     with open(f"{file}", "w") as file:
#         file.write(letter)

if not os.path.exists("letters"):
    os.mkdir("letters")
    for letter in string.ascii_letters:
        with open("letters/" + letter + ".txt", "w") as file:
            file.write(letter + "\n")
