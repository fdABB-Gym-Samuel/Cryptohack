from Crypto.Cipher import AES
from pwn import xor
import os

KEY = b"a"*16
FLAG = "This is a test!!" + "b"*16
iv = os.urandom(16)

def decrypt(ciphertext, KEY, iv):
    ciphertext = bytes.fromhex(ciphertext)

    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}


def encrypt(KEY, iv):
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(FLAG.encode())
    ciphertext = iv.hex() + encrypted.hex()

    return {"ciphertext": ciphertext}


ct = encrypt(KEY, iv)["ciphertext"]
pt = decrypt(ct, KEY, iv)["plaintext"]

print(iv.hex())
print(ct)
print(pt)
print(xor(bytes.fromhex(pt), iv))