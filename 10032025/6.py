from turtle import *
lt(90)
size=30
screensize(canvwidth=2000, canvheight=2000)
tracer(0)
down()
for i in range(9):
    fd(size * 22)
    rt(90)
    fd(size * 6)
    rt(90)
up()
fd(size * 1)
rt(90)
fd(size * 5)
lt(90)
down()
for i in range(9):
    fd(53 * size)
    rt(90)
    fd(75 * size)
    rt(90)
up()
for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x * size, y * size)
        dot(10, 'red')
done()