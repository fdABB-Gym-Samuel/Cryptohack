from pwn import xor
ct = "c52c095d918a039987cee38eda4b73a339dabd6873c956b92ff0a577386033be2b832fd7219c0c9499b2ff446a70e15f"
pt = "2e7fbeb4f8307827d55e86a81529fcb5a65e702de5e578aae4acbcbbaf28189666eecb5842ad098818af8456194112c3"

iv = ct[:32]

p1_clean = xor(bytes.fromhex(pt), bytes.fromhex(iv)) # leaks first 16 bytes of message

# p1 = b"crypto{3cb_5uck5"
c1 = ct[32:64]
p2 = pt[64:96]
p2_clean = xor(bytes.fromhex(p2), bytes.fromhex(c1)) # b'_4v01d_17_!!!!!}'

print(p1_clean + p2_clean) # ... crypto{3cb_5uck5 ... _4v01d_17_!!!!!}
# crypto{3cb_5uck5_4v01d_17_!!!!!}

# This test became a solution :)
