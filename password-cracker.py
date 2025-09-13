import csv
import hashlib
from csv import DictReader

username_hash_dict = {}

with open('common-passwords.txt', 'r') as file:
    common_passwords = file.read().splitlines()

with open('username-hashes.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        username_hash_dict[row["username"]] = row["hash"]

for password in common_passwords:
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    for username, hash in username_hash_dict.items():
        if hashed_password == hash:
            print(f"Found credentials for: {username}, {password}")
