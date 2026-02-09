otv = c = 10**10
for n in range(20,2000):
    s = oct(n)[2:]
    if n%7==0:
        s = s + s[-2:]
    else:
        s = oct((n%7)*7)[2:] + s
    r = int(s,8)
    if r > 500 and c > r:
        otv = n
        c = r
print(otv)