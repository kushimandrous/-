from itertools import*
s = 'буржазия'
c = 0
for i in product(s,repeat=8):
    if 'буржуи' not in s:
        c +=1
print(c)
    #16777216