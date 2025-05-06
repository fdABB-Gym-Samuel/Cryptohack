# As we've seen, we can work within a finite field Fp​, adding and multiplying elements, and always obtain another element of the field.

# For all elements g in the field, there exists a unique integer d such that g ⋅ d ≡ 1 mod p.

# This is the multiplicative inverse of g.

# Example: 7 ⋅ 8 = 56 ≡ 1 mod 11

# What is the inverse element: d = 3^−1 such that 3 ⋅ d ≡ 1 mod 13?

# a^(p-1) = 1 mod p 
# =>
# Multiply both sides with 1/a
# a^(p-1) * a^(-1)= a^(-1) mod p
# =>
# Break out a from a^(p-1) to get a^(p-2) * a
# a^(p-2) * a * a^(-1) = a^(-1) mod p
# =>
# a * a^(-1) = a * 1/a = a/a = 1
# a^(p-2) = a^(-1) mod p
# =>
# a^(p-2) mod p = a^(-1)

# 3 * d = 1 mod 13
# =>
# 3^(13 - 1) = 1 mod 13
# 3^(13 - 2) * 3 = 1 mod 13
# 3^(13 - 2) * 3 * d = d mod 13
# 3^(13 - 2) = d mod 13
# d = 3^(13 - 2) mod 13
# 

print(pow(3, 13-2, 13)) # 9