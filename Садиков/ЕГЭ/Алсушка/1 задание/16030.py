from itertools import*
s = '56 347 257 26 136 145 23'.split()
v = 'bd dc bf cg ce eg gf fa ab'.split()
print('1 2 3 4 5 6 7')
for p in permutations('bdcegfa'):
    if all(str(p.index(b)+1) in s[p.index(a)] for a,b in v):
        print(*p)
        