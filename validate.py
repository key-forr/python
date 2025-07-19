email = input("What's your enail address? ").strip()

def validate_email(email):
    if "@" not in email or email.count("@") != 1:
        return "Invalid"
    
    name, domain = email.split("@")

    if not name:
        return "Invalid"
    
    if "." not in domain:
        return "Invalid"
    
    parts = domain.rsplit(".", 1)
    if len(parts) != 2 or not parts[0] or not parts[1]:
        return "Invalid"
    

    return "Valid"

result = validate_email(email)
print(result)