from turtle import *
lt(90)
size=30
screensize(2000,2000)
tracer(0)
down()
rt(45)
for i in range(7):
    fd(5*size)
    rt(45)
    fd(10 * size)
    rt(135)
up()
for x in range(-20,20):
    for y in range(-20,20):
        setpos(x*size,y*size)
        dot(4,'red')
done()