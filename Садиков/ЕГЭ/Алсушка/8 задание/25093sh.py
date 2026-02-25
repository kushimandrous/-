from itertools import*
s = 'мыши'
c = 0
for i in product(s,repeat=7):
    if 'мыш' in i:
        c+=1
print(c)
