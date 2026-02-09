a=[]
for i in range(1,101):
    n = bin(i)[2:]
    s = n +str(n.count('1')%2)
    r = n +str(n.count('1')%2)
    r1=int(r,2)
    if r1>123:
        print(r1)
        

    


