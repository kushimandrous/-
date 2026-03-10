a=[]
for m in range(0,50,2):
    for n in range(1,50,2):
        x = 2**m * 3**n
        if 400000000<= x <=600000000:
            a.append(x)
print(*sorted(a))