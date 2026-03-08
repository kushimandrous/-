from itertools import*
s = '24 146 45 12356 34 24 '.split()
v = ' cd de db cb be ba ag gb'.split()
print('1 2 3 4 5 6')
for p in permutations('dcebag'):
    if all(str(p.index(b)+1) in s[p.index(a)] for a,b in v):
        print(*p)
        break