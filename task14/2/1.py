for x in range(0, 20):
    a = int('12345078', 20) + x * 20**2
    b = int('90765', 20) + x * 20**3
    n = a + b
    if n % 19 == 0:
        print(x, n // 19)