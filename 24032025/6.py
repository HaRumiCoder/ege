from turtle import *
lt(90)
size=30
screensize(canvwidth=3000, canvheight=3000)
tracer(0)
down()
rt(180)
fd(2 * size)
rt(90)
fd(40 * size)
rt(90)
fd(2 * size)
for i in range(4):
    seth(90)
    circle(-5*size, 180)
up()
for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x * size, y * size)
        dot(10, 'red')
done()