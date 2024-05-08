from string import digits, ascii_uppercase


def n_to_p(n, p):
    r = ''
    # alp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alp = digits + ascii_uppercase
    while n:
        r = alp[n % p] + r
        n //= p
    return r


def f(n):
    s1 = n_to_p(n, 3)
    s2 = s1 + s1[-1] * 3
    return int(s2, 3)


a = []
for i in range(1, 1000):
    res = f(i)
    if 1000 <= res <= 9999:
        a.append(res)
print(min(a))
