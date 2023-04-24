with open("URL_Cleaner.txt", "r") as file:
    lines = file.readlines()

print(lines)

with open("URLS_Corrected.txt", "w") as file:
    for line in lines:
        line_remove_s = line.replace("s", "", 1)
        line_remove_s_add_line = line_remove_s[:6] + "/" + line_remove_s[6:]
        file.write(line_remove_s_add_line)
