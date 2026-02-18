from turtle import*
screensize(2000,2000)
tracer(0)
m=30
lt(90)
pd()

for i in range(4):
    for u in range(2):
        fd(2*m)
        rt(45)
        fd(2*m)
        lt(90)
    rt(180)

pu()

for x in range(-30,30):
    for y in range(-30,30):
        goto(x*m,y*m)
        dot(5)

done()
#16