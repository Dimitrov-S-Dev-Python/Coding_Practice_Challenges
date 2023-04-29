# from csv import writer
# write a new file

# with open("test.csv", "w") as file:
#     data = writer(file)
#     data.writerow(["first_name", "last_name"])
#     data.writerow(["Sancho", "Pansa"])
#     data.writerow(["Carabas", "Barabas"])
#

# open and write existing

from csv import reader, writer

with open("fighters.csv", "r") as file:
    content = reader(file)
    info = [[s.upper() for s in row ] for row in content]


with open("test.csv", "w", newline="") as file:
    data = writer(file)
    for header in info:
        data.writerow(header)

