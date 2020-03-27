# Use pow(x, y, mod).

def modpow(a, b, mod=1000000007):
    res = 1
    while b:
        if b & 1: res = res * a % mod
        a = a * a % mod
        b >>= 1
    return res