from turtle import *
lt(90)
size=30
screensize(canvwidth=2000, canvheight=2000)
tracer(0)
down()
for i in range(9):
    fd(size * 9)
    rt(90)
    fd(size * 3)
    rt(90)
up()
for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x * size, y * size)
        dot(10, 'red')
done()