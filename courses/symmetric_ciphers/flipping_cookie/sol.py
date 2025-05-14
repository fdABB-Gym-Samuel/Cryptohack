from Crypto.Cipher import AES
import os
from Crypto.Util.Padding import pad, unpad
from datetime import datetime, timedelta

# # cookie = requests.get("https://aes.cryptohack.org/flipping_cookie/get_cookie").json()["cookie"]
# # print(cookie) #b274fc86da5fa495bcf354aaa38883917ede42b8aee9ebffe1a06ae40bff9a992617c2b99f8f7191070b5839c4a715b5
# cookie = "b274fc86da5fa495bcf354aaa38883917ede42b8aee9ebffe1a06ae40bff9a992617c2b99f8f7191070b5839c4a715b5"

# # expires_at = (datetime.today() + timedelta(days=1)).strftime("%s")
# # expires_at = int((datetime.today() + timedelta(days=1)).timestamp())
# expires_at = 1747325996
# pt_cookie = f"admin=False;expiry={expires_at}".encode()
# # print(pt_cookie)

# cookie_bites = bytes.fromhex(cookie)
# print(cookie_bites)

# cookie_bites = b'\x01\xd4\x86\x91\xb6@\xa5\xfc\xa3aW+\x86\xd8\xb7d\xce\x95\x8eZ\xaf\xe6ap\x8d\xe69\xee\xd11\xd6\xe4\xc7\xba\xed\xd0RCqq\xc1\x0484/\xa80<'
# iv = cookie_bites[:8]
# print(len(cookie_bites[8:]))



KEY = b"oknydfghjkupsxcv"
FLAG = "sppppppppppppppppppppp"


def check_admin(cookie, iv):
    cookie = bytes.fromhex(cookie)
    iv = bytes.fromhex(iv)

    try:
        cipher = AES.new(KEY, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(cookie)
        unpadded = unpad(decrypted, 16)
        print(decrypted)
    except ValueError as e:
        return {"error": str(e)}

    if b"admin=True" in unpadded.split(b";"):
        return {"flag": FLAG}
    else:
        return {"error": "Only admin can read the flag"}


def get_cookie():
    # expires_at = int((datetime.today() + timedelta(days=1)).timestamp())
    expires_at = 1747327852
    cookie = f"admin=False;expiry={expires_at}".encode()

    iv = os.urandom(16)
    padded = pad(cookie, 16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(padded)
    ciphertext = iv.hex() + encrypted.hex()

    return ciphertext

cookie = get_cookie()
print(cookie, "ecrtvybunhjmi")
check_admin(cookie, cookie[:32])



