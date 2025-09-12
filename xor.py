import string
from pwn import *


charset = string.ascii_letters + string.digits
enc_flag = bytes.fromhex("191d7c32197c345d271d082d45081d396152220a0c3b437a08211948213c3f2148791c3f2d7e3b14")
part_flag = b"THM{"

part_key = xor(enc_flag, part_flag)[:4]

print(part_key)

for c in charset:
    key = part_key + c.encode()
    dec_flag = xor(enc_flag, key).decode()

    if dec_flag[-1] == '}':
        print(f"Key: {key.decode()}")
        print(f"Flag: {dec_flag}")
