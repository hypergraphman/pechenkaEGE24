from math import ceil

_, *a = map(int, open('26.txt'))
a.sort()
s = 0
while a[0] <= 500:
    s += a.pop(0)
x = len(a) // 2
print(s + ceil(sum(a[:x]) * 0.8) + sum(a[x:]))
print(a[x - 1])
