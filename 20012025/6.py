from turtle import *
lt(90)
size = 30
screensize(2000, 2000)
tracer(0)
down()
for i in range(4):
    fd(7*size)
    rt(90)
    fd(8*size)
    rt(90)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(y*size, x*size)
        dot(10, 'red')
done()