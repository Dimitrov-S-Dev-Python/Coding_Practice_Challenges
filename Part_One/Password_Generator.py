# Create a program that generates a pass of 6 random alphanumeric characters
import string
import random

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
chosen = random.sample(characters, 6)

password = "".join(chosen)
print(password)
