k = 0
for x in range(-100, 100):
    for y in range(-100, 100):
        if 0 <= x <= 13 and -20 <= y <= 0 or 8 <= x <= 8 + 16 and -5 <= y <= 3:
            k += 1
print(k)