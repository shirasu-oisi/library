N = 510000
fac = [1, 1] # 0 <= k < N; k!
finv = [1, 1] # 0 <= k < N; (k!)^(-1) (mod p)
inv = [0, 1] # 1 <= k < N; k^(-1) (mod p)

MOD = 10**9 + 7

# nPk = n! * ((n-r)!)^(-1)
# nCk = n! * (k!)^(-1) * ((n-k)!)^(-1)
# nHk = (n+r-1)Cr = (n+r-1)! * (r!)^(-1) * ((n-1)!)^(-1)

for i in range(2, N):
    fac.append(fac[i-1]*i % MOD)
    inv.append(MOD - inv[MOD%i] * (MOD//i) % MOD)
    finv.append(finv[i-1]*inv[i] % MOD)

def nCr(n, r):
    if n < r or n < 0 or r < 0: return 0
    return fac[n] * (finv[r] * finv[n-r] % MOD) % MOD

def nPr(n, r):
    if n < r or n < 0 or r < 0: return 0
    return fac[n] * finv[n-r] % MOD

def nHr(n, r):
    return C(n+r-1, r)

print(nCr(100000, 50000))
