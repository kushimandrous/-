def f(n):
    s =set()
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    return s 

maxl=0
minn=0
for n in range(84052,84130+1):
    b = f(n)
    if b:
        if len(b)>maxl:
             maxl=len(b)
             minn=n
        elif len(b)==maxl and n<minn:
            minn = n 

print(maxl,minn) #72 84084