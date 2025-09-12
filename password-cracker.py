import hashlib

test_password = 'my_passwd'
test_hash_obj = hashlib.sha224(test_password.encode('utf-8'))
digest = test_hash_obj.hexdigest()

print(digest) # 4b18bf88fab81f30a3bcf3de9397ab4aff16545694dc733ab6630efd