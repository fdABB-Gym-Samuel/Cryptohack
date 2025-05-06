from pwn import *
in_data = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
in_data = bytes.fromhex(in_data)
_format_start = "crypto{"
_format_end = "}"
key_start = xor(_format_start, in_data[:len(_format_start)])
key_end = xor(_format_end, in_data[-1])
print(f"Key_format: {key_start}...{key_end}")
# This should only work when the key is smaller than how much we know
key_complete = key_start + key_end

print(xor(in_data, key_complete))
print(len(_format))
