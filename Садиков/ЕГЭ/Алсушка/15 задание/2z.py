g = []
for a in range(1,63):
    count = 0
    for x in range(1,1001):
        p = (x & a)!=0
        q = ( x & 28) == 0
        r = (x & 53) != 0
        s = ( x &  20) == 0
        if ((not p) or (not q) or ( r and s)) == 1:
            count = count + 1
    if count==1000:
        g.append(a)
print(max(g))