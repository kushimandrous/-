from turtle import*
screensize(5000,5000)
tracer(0)
m=30
left(90)
pd()

for i in range(4):
    rt(90)
    for u in range(4):
        fd(4*m)
        rt(315)
    rt(90)

pu()

for x in range(-80,80):
    for y in range(-80,80):
        goto(x*m,y*m)
        dot(5)
done()


