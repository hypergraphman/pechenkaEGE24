def med(a):
    if len(a) % 2 != 0:
        return a[len(a) // 2]
    return sum(a[len(a) // 2 - 1:len(a) // 2 + 1]) / 2


f = open('26.txt')
p, n = map(int, f.readline().split())
N = 10001
data = [[] for _ in range(N)]
# data = []
# for _ in range(4):
#     data.append([])
print(data)
for line in f:
    i, m = map(int, line.split())
    data[i].append(m * 100)
print(data)
min_avg = float('inf')
max_d = 0
max_id = 0
for i in range(1, N):
    if len(data[i]) != 0:
        data[i].sort()
        x = len(data[i]) * p // 100
        if x != 0:
            data[i] = data[i][x:-x]
        avg = sum(data[i]) / len(data[i])
        min_avg = min(avg, min_avg)

        d = abs(avg - med(data[i]))
        if d >= max_d:
            max_d = d
            max_id = i

print(int(min_avg), max_id)
