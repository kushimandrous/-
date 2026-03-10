def f(n):
    s = set()
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    if len(s)==4:return s 
    else:return 0

k = 0
for x in range(210235,210300+1):
    m = f(x)
    if m!=0:
        print(m)

