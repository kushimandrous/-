def f(a,b,m):
    if a+b>=43: return m%2==0
    if m==0: return 0
    h = [f(a+2,b,m-1),f(a,b+2,m-1),f(a*3,b,m),f(a,b*3,m)]
    return any(h) if m%2!=0 else all(h)


print([ s for s in range(1,37) if not f(6,s,1) and f(6,s,2)])
print([ s for s in range(1,37) if not f(6,s,1) and f(6,s,3)])
print([ s for s in range(1,37) if not f(6,s,2) and f(6,s,4)])