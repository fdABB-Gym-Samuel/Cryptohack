from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import requests

KEY = b"HELLO_this_is_me"
FLAG = "crypto{this iss a testing flaggging}"
URL_BASE = "https://aes.cryptohack.org/ecb_oracle/"
def encrypt(plaintext):
    # if len(plaintext) < 2:
    #     raise Exception("THis wont woRk iN ProDuCTIOn!1!")
    # plaintext = bytes.fromhex(plaintext)

    # padded = pad(plaintext + FLAG.encode(), 16)
    # print(padded)
    # print(" ")
    # cipher = AES.new(KEY, AES.MODE_ECB)
    # try:
    #     encrypted = cipher.encrypt(padded)
    # except ValueError as e:
    #     return {"error": str(e)}

    # return encrypted.hex()
    return requests.get(URL_BASE + "encrypt/" + plaintext).json()["ciphertext"]

# print(f"{ord(' '):02x}")
# shit = "".join([f"{ord(char):02x}" for char in FLAG[:15]])
# print(encrypt("00"*16)[32:])
# print(encrypt("00"*16 + shit + "20")[32:])


valid_chars = list("1234567890abcdefghijklmnopqrstuvwxyz{}_-[]()?!ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
known_flag = []
current_block = 0
done = False
# done = True
print(valid_chars)
while not done:

    orig_padd = "00"*(15-(len(known_flag) % 16))
    if len(orig_padd) == 0:
        orig_padd = "00" * 16

    original = encrypt(orig_padd)
    important_orig_block = original[32*current_block:32+32*current_block]
    print(b"".join([bytes.fromhex(cr) for cr in known_flag]))
    for char in valid_chars:
        # current_block = len(known_flag) // 15

        test_padd = orig_padd + "".join(known_flag) + f"{ord(char):02x}"
        test = encrypt(test_padd)
        important_test_block = test[32*current_block:32+32*current_block]

        if important_orig_block == important_test_block:
            # print(important_orig_block)
            # print(original)
            # print()
            # print()
            # print(important_test_block)
            # print(test)
            # print(current_block)
            # print(len(known_flag))
            # print(char)
            known_flag.append(f"{ord(char):02x}")

            current_block = len(known_flag) // 15

            if char == "}":
                done = True

            break
    # if current_block == 1:
    #     break
    # break