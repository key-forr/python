import hashlib

password1 = "welcome1"
password2 = "python is the best"
password3 = "password123"

hash1 = hashlib.sha256(password1.encode('utf-8'))
hash2 = hashlib.sha256(password2.encode('utf-8'))
hash3 = hashlib.sha256(password3.encode('utf-8'))

print(hash1.hexdigest())
print(hash2.hexdigest())
print(hash3.hexdigest())

print(hash1)
print(hash2)
print(hash3)