from itertools import*
s = '24567 146 5 12 1367 125 15'.split()
v = ' аб бв бе еж жв гд дж де'.split()
print('1 2 3 4 5 6 7 ')
for p in permutations('абвгдже'):
    if all(str(p.index(b)+1) in s[p.index(a)] for a,b in v):
        print(*p)