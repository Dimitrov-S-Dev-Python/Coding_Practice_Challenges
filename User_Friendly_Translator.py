d = dict(weather = "clima", earth = "terra", rain = "chuva")

def get_translator(word):
    try:
        return d[word]
    except KeyError:
        return "We couldn't find that word!"

user_input = input("Enter a word:")
user_input.strip().lower()

print(get_translator(user_input))
