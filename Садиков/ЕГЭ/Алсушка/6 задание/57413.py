from turtle import*
tracer(0)
m = 50
screensize(5000,5000)
left(90)
pd()


rt(45)
for i in range(7):
    fd(5*m)
    rt(45)
    fd(10*m)
    rt(135)


pu()


for x in range(-20,20):
    for y in range(-20,20):
        setpos(x*m,y*m)
        dot(5)
done() #27