def fib(n, MOD=10**9+7):
    if n<0: return
    a, b, c, d = 0, 1, 1, 1
    ra, rb, rc, rd = 1, 0, 0, 1
    while n:
        if n & 1: ra, rb, rc, rd = (ra*a+rb*c)%MOD, (ra*b+rb*d)%MOD, (rc*a+rd*c)%MOD, (rc*b+rd*d)%MOD
        a, b, c, d = (a*a+b*c)%MOD, (b*a+b*d)%MOD, (c*a+c*d)%MOD, (d*d+b*c)%MOD
        n >>= 1
    return rb