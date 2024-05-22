from itertools import product

words = [''.join(word) for word in product(sorted('СНЕГУРОЧКА'), repeat=5)]

# words = []
# alf = sorted('СНЕГУРОЧКА')
# for word in product(alf, repeat=5):
#     t = ''.join(word)
#     words.append(t)

k = 0
for word in words:
    if 'РУЧКА' <= word <= 'ЧУКЧА':
        k += 1
print(k)