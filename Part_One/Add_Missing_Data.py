checklist = ["Portugal", "Germany", "Spain"]
checklist = [i + "\n" for i in checklist]

with open("Add_Missing_data.txt", "r") as file:
    content = file.readlines()

updated_list = sorted(checklist + content)

with open("Countries_missing_fixed", "w") as file:
    for item in updated_list:
        file.write(item)
