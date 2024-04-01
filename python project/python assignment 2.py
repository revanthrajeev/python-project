import re

def validate_password(password, username, last_three_passwords):
    
    if len(password) < 10:
        print("Password must be at least 10 characters long.")
        return False
    
    
    if not (re.search(r"[A-Z].*[A-Z]", password) and
            re.search(r"[a-z].*[a-z]", password) and
            re.search(r"\d.*\d", password) and
            re.search(r"[!@#$%^&*].*[!@#$%^&*]", password)):
        print("Password must contain at least two uppercase letters, two lowercase letters, two digits, and two special characters.")
        return False
    
    
    for i in range(len(password) - 2):
        if password[i:i+3] in username:
            print("Password should not contain any sequence of three or more consecutive characters from the username.")
            return False
    if re.search(r"(.)\1\1\1", password):
        print("No character should repeat more than three times in a row.")
        return False
    
    
    if password in last_three_passwords:
        print("Password must not be the same as the last three passwords used.")
        return False
    
    
    return True

def main():
    username = input("Enter username: ")
    last_three_passwords = []
    
    while True:
        password = input("Enter new password: ")
        if validate_password(password, username, last_three_passwords):
            print("Password set successfully.")
            last_three_passwords.append(password)
            if len(last_three_passwords) > 3:
                last_three_passwords.pop(0)
            break

if __name__ == "__main__":
    main()
