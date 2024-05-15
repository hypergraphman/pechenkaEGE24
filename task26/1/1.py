with open('26.txt') as f:
    s, n = map(int, f.readline().split())
    *a, = map(int, f)
print(a[:10])