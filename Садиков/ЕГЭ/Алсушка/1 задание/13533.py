from itertools import*
s = '248 13 268 17 678 358 45 1345'.split()
v = 'аб аг ав ве ег бг бд дк кл ле гд'.split()
print('1 2 3 4 5 6 7 8')
for p in permutations('абвгдекл'):
    if all(str(p.index(b)+1)in s[p.index(a)] for a,b in v):
        print(*p)