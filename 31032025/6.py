from turtle import *
lt(90)
size=30
screensize(canvwidth=3000, canvheight=3000)
tracer(0)
down()
rt(90)
for i in range(4):
    fd(4*(5**0.5)*size)
    rt(150)
    fd(4 * (5 ** 0.5)*size)
    rt(300)
up()
for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x * size, y * size)
        dot(10, 'red')
done()