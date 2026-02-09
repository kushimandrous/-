from itertools import *
s = '347 356 124567 13 23 237 136'.split()
v = 'gd dc df gf cf ef eb bf ba af ag'.split()
print(*range(1,8))
for p in permutations('abcdefg'):
    if all(str(p.index(b)+1) in s[p.index(a)] for a,b in v):
        print(*p)
        break