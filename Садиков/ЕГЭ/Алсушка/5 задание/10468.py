
for i in range (1,50):
    n=bin(i)[2:]
    r =n+str(n.count('1')%2)
    r =n+str(n.count('1')%2)
    print(i,int(n,2),int(r,2))



