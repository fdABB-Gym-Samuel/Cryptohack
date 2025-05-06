import base64

in_data = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
in_data = bytes.fromhex(in_data)
in_data = base64.b64encode(in_data)
print(in_data)