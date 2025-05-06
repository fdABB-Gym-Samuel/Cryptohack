in_data = "label"
key = 13

out = "".join([chr(ord(char) ^ key) for char in in_data])
print(out)