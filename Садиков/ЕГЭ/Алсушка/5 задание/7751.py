a = []
for n in range(1000,10000):
    s = str(n)
    r1 = int(s[0]) + int(s[1])
    r2 = int(s[2]) + int(s[3])
    min_a = min(r1,r2)
    max_a = max(r1, r2)
    result = str(min_a) + str(max_a)
    if result == '117':
        a.append(n)
print(a)