m = []

for s in open("C:\\Users\\kushi\\Desktop\\alsukege\9_24360.csv"):
    a = sorted([int(x) for x in s.split(';' \
    '+')])
    k = 0
    for x in set(a):
        k += a.count(x)//2
    if (a[0]**2 in a)+(k>=3)==1:
        m.append(sum(a))
print(min(m))