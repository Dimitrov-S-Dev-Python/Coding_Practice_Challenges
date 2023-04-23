import string

word_one = string.ascii_lowercase[::2]
word_two = string.ascii_lowercase[1::2]

for a, b in zip(word_one, word_two):
    text = f"{a}{b}"
    with open("result.txt", "a") as file:
        file.write(f"{text}" + "\n")
