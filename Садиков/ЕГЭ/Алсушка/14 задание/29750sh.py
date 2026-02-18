s = 25**20+4**11 - 2
m = ''
while s>0:
    m = m+ str(s%5)
    s//=5
print(s)
t = m.count('3')
print(t)
#2