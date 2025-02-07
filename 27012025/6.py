from turtle import *
lt(0)
size=30
screensize(canvwidth=2000, canvheight=2000)
tracer(0)
down()
for i in range(2):
    fd(15 * size)
    rt(90)
    fd(8 * size)
    rt(90)
lt(90)
fd(0.5 * size)
rt(90)
for i in range(2):
    fd(8 * size)
    rt(90)
    fd(15 * size)
    rt(90)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        setpos(x*size, y*size)
        dot(10, 'red')
done()