from itertools import*
s = '24 146 45 12356 34 24'.split()
v = 'ab bc cd db de eb bg ga'.split()
print (*range(1,7))
for p in permutations('abcdeg'):
    if all(str(p.index(b)+1)in s[p.index(a)]for a,b in v):
        print(*p)
        break