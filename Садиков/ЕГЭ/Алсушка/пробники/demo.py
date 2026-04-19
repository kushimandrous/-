'''from itertools import*
tab = '258 17 56 68 138 347 26 145'.split()
pic = 'hf hd hb fe eg gc cb ca ga ad'.split()
print('1 2 3 4 5 6 7 8')
for p in permutations('abcdefgh'):
    if all(str(p.index(b)+1) in tab[p.index(a)] for a,b in pic):
        print(*p)'''

'''print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if ((x or y) and(y!=z) and(not w))==1:
                    print(x,y,w,z)'''


'''for i in range(1,100):
    n = bin(i)[2:]
    if i%3==0:
        r = n + n[-3:]
    else:
        r = n+ bin((i%3)* 3 )[2:]
    r1 = int(r,2)
    if r1>=200:
        print(i)'''


'''from turtle import*
screensize(5000,5000)
tracer(0)
m = 30
lt(90)
pd()

for i in range(2):
    fd(14*m)
    lt(270)
    bk(12*m)
    rt(90)
pu()
fd(9*m)
rt(90)
bk(7*m)
lt(90)
pd()
for p in range(2):
    fd(13 * m)
    rt(90)
    fd(6 * m)
    rt(90)

pu()
for x in range(-70,70):
    for y in range(-70,70):
        goto(x*m,y*m)
        dot(5)
done()'''



'''from itertools import*
r = 0
for p in product('акорст', repeat = 5):
    p1 = ''.join(p)
    r+=1
    if r%2==0 and  p[0] not in ('а', 'с', 'т') and p.count('о')==2:
        print(p,r)'''

'''print((11*2**30)/(3845627))
print(3072*8)
print((3072*8)/2783)
print(2**9)
print(2**8)'''


