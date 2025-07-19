import re

email = input("What's your enail address? ").strip()

def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if re.fullmatch(pattern, email):  
        return "Valid"
    return "Invalid"



result = validate_email(email)
print(result)