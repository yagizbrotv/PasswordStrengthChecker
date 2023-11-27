import re

def check_password_strength(password):
    if len(password) < 8:
        return "Password is too short. It should be at least 8 characters long."

    if not any(char.isupper() for char in password):
        return "Password should contain at least one uppercase letter."

    if not any(char.islower() for char in password):
        return "Password should contain at least one lowercase letter."

    if not any(char.isdigit() for char in password):
        return "Password should contain at least one digit."

    special_characters = r"[!@#$%^&*(),.?\":{}|<>]"
    if not re.search(special_characters, password):
        return "Password should contain at least one special character."

    return "Password strength is sufficient."

while True:
    password_input = input("Enter your password: ")
    result = check_password_strength(password_input)
    
    if "sufficient" in result.lower():
        print("Password accepted. Thank you!")
        break
    else:
        print(f"Password not sufficient. {result}\nPlease try again.")
