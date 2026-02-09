g = []
for a in range(1,1000):
    count = 0
    for x in range(1,101):
        for y in range(1,101):
            if ((2*x - y >= a) and (y >=17) and ( 78>=x)) == 0:
                count = count + 1
    if count == 10000:
        g.append(a)
print(g)