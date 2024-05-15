def n_to_p(n, p):
    res = []
    while n:
        res = [n % p] + res
        n //= p
    return res


def sum_odd(a):
    s = 0
    for el in a:
        if el % 2 != 0:
            s += el
    return s


def sum_even(a):
    s = 0
    for el in a:
        if el % 2 == 0:
            s += el
    return s


def p_to_n(a, p):
    res = 0
    for el in a:
        res = res * p + el
    return res


def f(n):
    new_n = n_to_p(n, 80)
    for _ in range(2):
        # odd = sum_odd(new_n)
        odd = sum(filter(lambda x: x % 2, new_n))
        # even = sum_even(new_n)
        even = sum(filter(lambda x: x % 2 == 0, new_n))
        if odd > even:
            new_n += [n_to_p(odd, 80)[-1]]
        else:
            new_n += [n_to_p(even, 80)[-1]]
    return p_to_n(new_n, 80)


n = 1
while f(n) <= 10**6:
    n += 1
print(n)