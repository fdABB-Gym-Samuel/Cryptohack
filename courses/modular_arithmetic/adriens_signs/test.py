import random

# These to numbers will always give one i that can give the same result as res 2 but three that can give the same as res 1
# a = 1234
# p = 46091

a = 288260533169915
p = 1007621497415251
# a = 523635
# p = 9047509

e = random.randint(1, p)
res_1 = pow(a, e, p)
res_2 = (- pow(a, e, p) % p)

# What numbers can a^e mod p be?
flag = b"Abc"
plaintext = ''.join([bin(i)[2:].zfill(8) for i in flag])

# print(plaintext[:8])
# # print(res_1)
# # print(res_2)
# print(p/a)
for i in range(p):
    _ = pow(a, i, p)
    __ = - pow(a, i, p) % p
    print(_)
    print(__)
    print()
    # print()
    if i >= 25:
        break
    # if _ == res_2:
    #     print(i)

    # if i % 1000000 == 0:
    #     print(i)