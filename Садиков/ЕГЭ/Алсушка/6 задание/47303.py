from turtle import*
tracer(0)
m = 15
screensize(2000,2000)
left(90)
pd()
for i in range(4):
    fd(5*m)
    rt(90)
    fd(10*m)
    rt(90)

pu()
for x in range(-20-20):
    for y in range(-20,20):
        goto(x*m,y*m)
        dot(5)
done()