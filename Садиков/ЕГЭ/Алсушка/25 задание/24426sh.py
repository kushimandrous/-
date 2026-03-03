def f(n):
    s = set()
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    s = sorted(s)
    if len(s)==3: return s 
    else: return 0



k = 0
for n in range(10010,321341+1):
    if f(n):
        k+=1
        print(n,f(n),k) #2 но у меня 5 
       