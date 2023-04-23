import string

word_one = string.ascii_lowercase[::2]
word_two = string.ascii_lowercase[1::2]

for one, two in zip(word_one, word_two):
    text = f"{one}{two}"
    with open("result.txt", "a") as file:
        file.write(f"{text}" + "\n")
