from turtle import *

speed(0.00001)
cell = 20
for _ in range(2):
    fd(13 * cell)
    rt(90)
    fd(20 * cell)
    rt(90)
pu()
fd(8 * cell)
rt(90)
bk(3 * cell)
lt(90)
pd()
for _ in range(2):
    fd(16 * cell)
    rt(90)
    fd(8 * cell)
    rt(90)

pu()
for x in range(-3, 30):
    for y in range(-20, 5):
        goto(cell * x, cell * y)
        dot(5, 'red')
done()