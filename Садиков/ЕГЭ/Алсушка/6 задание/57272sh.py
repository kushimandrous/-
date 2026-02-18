from turtle import*
screensize(3000,3000)
tracer(0)
m=30
lt(90)
pd()

for i in range(2):
    fd(10*m)
    rt(90)
    fd(20*m)
    rt(90)

pu()

fd(5*m)
rt(90)
fd(7*m)
lt(90)

pd()
for u in range(2):
    fd(20*m)
    rt(90)
    fd(40)
    rt(90)



pu()

for x in range(-30,30):
    for y in range(-30,30):
        goto(x*m,y*m)
        dot(5)


done() #12