def extgcd(a, b):
    """
    Return a solution of ax + by = gcd(a, b)
    """
    a, b = (a, b) if a > b else (b, a)
    d = a // b
    p, q, r, s = 0, 1, 1, -d
    while a%b:
        a, b = b, a-b*d
        d = a // b
        p, q, r, s = r, s, p-r*d, q-s*d
    return p, q

