p = 29
# a_squared = 18
ints = [14, 6, 11]
a_s = []
for square in ints:
    for i in range(1, p):
        a = i if i * i % p== square else -1
        if a != -1:
            a_s.append(a)

print(a_s)

print(pow(21, 2, p))
