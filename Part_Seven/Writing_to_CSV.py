from csv import writer

with open("test.csv", "w") as file:
    data = writer(file)
    data.writerow(["first_name", "last_name"])
    data.writerow(["Sancho", "Pansa"])
    data.writerow(["Carabas", "Barabas"])