from turtle import *
lt(90)
size=30
screensize(canvwidth=2000, canvheight=2000)
tracer(0)
down()
for i in range(4):
    fd(6 * size)
    rt(150)
    fd(6 * size)
    rt(30)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        setpos(x*size, y*size)
        dot(10, 'red')
done()