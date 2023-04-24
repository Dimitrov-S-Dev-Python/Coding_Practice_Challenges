# Create a script that lets the user submit a pass until 3 conditions are met
# 1 contains at least one number
# 2 Has one uppercase letter
# 3 It is at least 5 chars long
# Print message "Password is not fine" if password is not correct

while True:
    psw = input("Enter your password: ")
    if any(i.isdigit() for i in psw) and any(i.isupper() for i in psw) and len(psw) >= 5:
        print("Password is fine")
        break
    else:
        print("Password is not fine")
