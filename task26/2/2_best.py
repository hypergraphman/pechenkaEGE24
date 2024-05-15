def med(a):
    if len(a) % 2 != 0:
        return a[len(a) // 2]
    return sum(a[len(a) // 2 - 1:len(a) // 2 + 1]) / 2


f = open('26.txt')
p, n = map(int, f.readline().split())
data = {}
print(data)
for line in f:
    i, m = map(int, line.split())
    if i not in data:
        data[i] = []
    data[i].append(m * 100)
print(data)
min_avg = float('inf')
max_d = 0
max_id = 0
for i in data:
    data[i].sort()
    x = len(data[i]) * p // 100
    if x != 0:
        data[i] = data[i][x:-x]
    avg = sum(data[i]) / len(data[i])
    min_avg = min(avg, min_avg)

    d = abs(avg - med(data[i]))
    if d > max_d:
        max_d = d
        max_id = i
    elif d == max_d:
        max_id = max(i, max_id)

print(int(min_avg), max_id)
