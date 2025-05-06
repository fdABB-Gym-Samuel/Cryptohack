import requests


URL_BASE = "https://aes.cryptohack.org"
encryption_endpoint = "/block_cipher_starter/encrypt_flag/"
ciphertext = requests.get(URL_BASE + encryption_endpoint).json()["ciphertext"]
print(ciphertext)

decryption_endpoint = "/block_cipher_starter/decrypt/"
flag = requests.get(URL_BASE + decryption_endpoint + ciphertext).json()["plaintext"]
print(bytes.fromhex(flag))