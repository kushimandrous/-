from turtle import*
screensize(3000,3000)
tracer(0)
m=30
lt(90)
pd()

for i in range(4):
    fd(10*m)
    rt(90)

pu()


for x in range(-30,30):
    for y in range(-30,30):
        goto(x*m,y*m)
        dot(5)

done() #81