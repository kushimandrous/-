from itertools import*
c = 0
for s in product('мангуст',  repeat=6):
    x = ''.join(s)
    if s[0] != 'а' and x.count('м') == 2 and x.count('у') != 0 and 'мм' not in x:
        c = c + 1

print(c)