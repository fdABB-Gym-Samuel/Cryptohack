from Crypto.Util.number import *
from pwn import *

in_data = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
in_data = bytes.fromhex(in_data)
print(in_data)
for i in range(255):
    out = xor(in_data, i).decode("utf-8")
    if out[:6] == "crypto":
        print(out)