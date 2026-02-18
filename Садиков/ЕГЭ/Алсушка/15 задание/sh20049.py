
def f(n,m):
    return n%m==0

for a in range(1,1000):
    ok = True
    for x in range(1,1000):
        if not( (not(f(x,45) and f(x,70))) or f(x,a)):
            ok = False
    if ok:
        print(a)
