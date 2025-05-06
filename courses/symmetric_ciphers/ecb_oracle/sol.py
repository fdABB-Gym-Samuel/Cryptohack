from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import requests

KEY = b"HELLO_this_is_me"
FLAG = "Crypto{this iss a testing flaggging}"
URL_BASE = "https://aes.cryptohack.org/ecb_oracle/"
def encrypt(plaintext):
    if len(plaintext) < 2:
        raise Exception("THis wont woRk iN ProDuCTIOn!1!")
    plaintext = bytes.fromhex(plaintext)

    padded = pad(plaintext + FLAG.encode(), 16)
    print(padded)
    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        encrypted = cipher.encrypt(padded)
    except ValueError as e:
        return {"error": str(e)}

    return encrypted.hex()

# known_flag = ['63', '72', '79', '70', '74', '6f', '7b', '70', '33', '6e', '36', '75', '31', '6e', '35']
known_flag = []
shit = True
valid_chars = list("1234567890[]{}-_?!#$abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ")
curren_block = 0
while shit:
    orig = encrypt("00"*(15-(len(known_flag)%15)))
    print(known_flag)
    padding = "00"*(15-(len(known_flag)%15))
    currently_encrypted = padding + "".join([cahr for cahr in known_flag])
    print(currently_encrypted)
    # break
    # orig = requests.get(URL_BASE + "encrypt/" + "00"*curren_block + "00"*(15-(len(known_flag) % 16)))

    print(URL_BASE + "encrypt/" + padding)
    
    # print(orig)
    # print(hex(00))
    # for char in range(256):
    for char in valid_chars:

        hex_str = f"{ord(char):02x}"
        # hex_str = f"{ord("C"):02x}"
        # print(hex_str)
        comp = encrypt("00"*(15-(len(known_flag)%15)) + "".join(known_flag[15*curren_block:15+15*curren_block]) + hex_str)
        # comp = requests.get(URL_BASE + "encrypt/" + "00"*curren_block + "00"*(15-(len(known_flag) % 16)) + "".join(known_flag) + hex_str).json()["ciphertext"]
        print(comp)
        print(orig)
        print("")
        print("")

        if comp[32*curren_block:32 + 32*curren_block] == orig[32*curren_block:32 + 32*curren_block]:
            print(b"".join([bytes.fromhex(cr) for cr in known_flag]))

            known_flag.append(f"{ord(char):02x}")
            if len(known_flag)% 16 == 0:
                curren_block += 1
                print(b"".join([bytes.fromhex(cr) for cr in known_flag]))
                
                # shit = False
            if char == "}":
                shit = False
                print(b"".join([bytes.fromhex(cr) for cr in known_flag]))

                # break

            # if len(known_flag) == 16:
            #     shit = False
            break
        
        # break
    # break

# print(encrypt(""))
# 16 null bytes becomes
#33591686ca590e42847c7a87919aaa96