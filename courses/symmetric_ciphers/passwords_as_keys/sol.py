import requests
from Crypto.Cipher import AES
import hashlib
URL_BASE = "https://aes.cryptohack.org"

FLAG_ENDPOINT = "/passwords_as_keys/encrypt_flag/"

ciphertext = requests.get(URL_BASE + FLAG_ENDPOINT).json()["ciphertext"]

def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    # print(password_hash)
    # key = bytes.fromhex(password_hash)
    key = password_hash

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return decrypted.hex()

with open("crypto_hack/courses/symmetric_ciphers/passwords_as_keys/words") as words:
    wordlist = [word.strip() for word in words.readlines()]


for word in wordlist:
    flag = decrypt(ciphertext, hashlib.md5(word.encode()).digest())
    flag = "".join([chr(x) for x in bytes.fromhex(flag)])
    if flag.startswith("crypto{"):
        print(flag)
        print(word)


