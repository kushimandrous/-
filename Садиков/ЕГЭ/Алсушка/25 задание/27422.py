def f(n):
    s = set()
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    s=sorted(s)
    if len(s)==2: return s 
    else: return 0


k = 0
for n in range(174457,174505+1):
    if f(n):
        k+=1
        print(n,f(n))
        if k==10:
            break