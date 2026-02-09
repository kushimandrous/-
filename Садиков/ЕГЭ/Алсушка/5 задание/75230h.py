def f (n, osn):
    s = ''
    while n>0:
        s+=str(n%osn)
        n//=osn
    s = s[::-1]
    return s
for n in range(1,200):
    s= f(n,5)
    if n%5==0 or n%5==2 or n%5==4:
        k = sum(map(int,s))
        s1=f(k,5)
        s+=s1
    if n%5==1 or n%5==3:
        s='21'+ s
        r = int(s,5)
    if r<=320:
        print(n)