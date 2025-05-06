# Lets say we pick p=17. Calculate 3^17 mod 17. Now do the same but with 5^17 mod 17 .

# What would you expect to get for 7^16 mod 17? Try calculating that.

# This interesting fact is known as Fermat's little theorem. We'll be needing this (and its generalisations) when we look at RSA cryptography.

# Now take the prime p=65537. Calculate 273246787654^65536 mod 65537.

# Did you need a calculator? 

print(3**17 % 17)
print(5**17 % 17)
print(7**16 % 17)

print(273245787654 ** 65536 % 65537)