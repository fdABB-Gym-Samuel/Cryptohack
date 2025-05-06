from Crypto.Util.number import *
import time
# x ≡ 2 mod 5
# x ≡ 3 mod 11
# x ≡ 5 mod 17

# Find the integer a such that x ≡ a mod 935

# x mod 5 = 2
# x mod 11 = 3
# x mod 17 = 5
# x mod a = 935

# Starting with the congruence with the largest modulus, use that for x ≡ a mod p we can write x = a + k ⋅ p for arbitrary integer k.

# x = a + k * 935 

# 5 * k_1 + 2 = x
# 11 * k_2 + 3 = x
# 17 * k_3 + 5 = x

n_biggest = 17
n_middle = 11
n_smallest = 5

n_s = [17, 11, 5]
a_s = [5, 3, 2]
start = time.time()
print((2*11*17*inverse(11*17, 5) + 3*5*17*inverse(5*17, 11) + 5*5*11*inverse(5*11, 17)) % 935)
print(f"took: {time.time() - start}")
start = time.time()
i = 0
while True:
    poss_x = i * n_s[0] + a_s[0]
    if (poss_x - a_s[1]) % n_s[1] == 0 and (poss_x - a_s[2]) % n_s[2] == 0:

        print("Maybe found:", poss_x)
        print("a?:", poss_x % 935)
        print(f"took: {time.time() - start}")
        break

    i += 1


