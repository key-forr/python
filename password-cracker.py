import hashlib

uppChar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowChar = "abcdefghijklmnopqrstuvwxyz"
numChar = "0123456789"
spcChar = "!@#$%^&*_-"

target = "6f0874bd7ba418106ac15555ea927aef34bc05c8ba92cd2e4c3065e7751ccc125fd88f19eec18f007e9f033c8dd2749edf573ac8aeec47d073f5832553fcea9c"

test_password = 'my_passwd'
test_hash_obj = hashlib.sha224(test_password.encode('utf-8'))
digest = test_hash_obj.hexdigest()

print(digest) # 4b18bf88fab81f30a3bcf3de9397ab4aff16545694dc733ab6630efd
