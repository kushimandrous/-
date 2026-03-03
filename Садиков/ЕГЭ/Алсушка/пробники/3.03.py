# print('x,y,z,w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (((x<=z)and(z<=w)) or ( y==(x or z)))==0:
#                     print(x,y,z,w)   #yzwx


# def f(n):
#     s = ''
#     while n>0:
#         s = str(n%3)+s
#         n//=3
#     return s 


# for i in range(1,1000):
#     g = f(i)
#     if i%5==0:
#         r = g +'02'
#     else:
#         r= g + str(f(((i%5)*3)))[-2:]
#     if int(r,3)==192:
#         print(int(r,3),i,r) #21


# from turtle import*
# screensize(3000,3000)
# tracer(0)
# m=30
# lt(90)


# pd()


# for c in range(2):
#     fd(21*m)
#     rt(90)
#     fd(27*m)
#     rt(90)


# pu()

# for i in range(9):
#     fd(9*m)
#     rt(90)
#     fd(10*m)
#     lt(90)


# pd()
# for z in range(2):
#     fd(86*m)
#     rt(90)
#     fd(47*m)
#     rt(90)


# pu()

# for x in range(-30,30):
#     for y in range(-30,30):
#         goto(x*m,y*m)
#         dot(5)


# done()

# from itertools import*
# c = 0
# for i in product('апрсу', repeat = 5):
#     c +=1
#     if i.count('у')==1 and i.count('а')==0:
#         print(i,c)



# def f(n):
#     s = ''
#     while n>0:
#         s = str(n%5)+s
#         n//=5
#     return s 

# for x in range(2,2026):
#     s = 5**2025 + 5**200 - x 
#     d = str(f(s))
#     max = -22222
#     if d.count('4')>max:
#         max = d.count('4')

# print(max) #196



