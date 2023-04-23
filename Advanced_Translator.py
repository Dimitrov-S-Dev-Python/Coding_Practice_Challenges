d = dict(weather = "clima", earth = "terra", rain = "chuva")

def vocabulary(word):
    try:
        return d[word]
    except KeyError:
        return "That word does not exist."


user_input = input("Enter a word: ")
user_input.strip()
print(vocabulary(user_input))
