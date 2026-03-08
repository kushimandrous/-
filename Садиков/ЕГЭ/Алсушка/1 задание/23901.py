from itertools import*
s = '36 4567 17 257 246 125 234'.split()
v = 'cf fb bg  de eg ae ab ad'.split()
print('1 2 3 4 5 6 7 ')
for p in permutations('cfbgeda'):
    if all(str(p.index(b)+1) in s[p.index(a)] for a,b in v):
        print(*p)