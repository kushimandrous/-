min=10*10
for i in range(1,200):
    n = bin(i)[2:]
    n+=n[-1]
    if n.count('1')%2==0:
        n+='0'
    else:
        n+='1'
    if n.count('1')%2==0:
        n+='0'
    else:
        n+='1'
    r = int(n,2)
    if r>204 and r<min:
        min=r
print(min)