from csv import reader

with open("fighters.csv", "r") as file:
    content = reader(file)
    next(content)
    for fighter in content:
        print(f"{fighter[0]} is from {fighter[1]}")
