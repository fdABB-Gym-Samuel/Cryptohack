import math
def euclids_alg(a, b):
    big, small = max(a, b), min(a, b)
    q = math.floor(big / small)
    r = big - small * q
    while True:
        big, small = small, r
        q = math.floor(big / small)
        r = big - small * q
        if r == 0:
            return small
if __name__ == "__main__":
    print(euclids_alg(66528, 52920))
