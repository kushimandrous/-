s = 12**16+12**22-78
m=''
while s>0:
    m = m+str(s%12)
    s//=12
    print(s,m)

t =m.count('0')
print('yes',t)#6