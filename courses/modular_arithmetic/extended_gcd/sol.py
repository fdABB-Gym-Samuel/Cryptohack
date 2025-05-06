import math

def euclids_alg_extended(a, b):
    
    big, small = max(a, b), min(a, b)
    org_big, org_small = big, small
    q = math.floor(big / small)
    r = big - small * q
    p_0 = 0
    p_1 = 1
    while True:
        p_0, p_1 = p_1, (p_0 - p_1*q) % org_big
        big, small = small, r
        q = big // small
        # Same as just using mod
        r = big - small * q
        if r == 0:
            op_1 = (small - org_small*p_1)/org_big
            op_2 = (small - org_big*p_1)/org_small
            v = op_1 if op_1*org_big + p_1*org_small == small else op_2
            if v != int(v):
                raise Exception("Damn, something went wrong while calculating v, for some reason its not an int. Well good luck")
            return small, p_1, int(v)



if __name__ == "__main__":
    p=26513
    q=32321
    p, q = max(p, q), min(p, q)

    gcd, u, v = euclids_alg_extended(p, q)
    
    print(f"a: {p}\nb: {q}\ngcd: {gcd}\nu: {u}\nv: {v}")
    # u, v = extended_euclid(p, q, gcd)
