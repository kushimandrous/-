s = 27**400-9**300-3**100+3**50
m=''
while s>0:
    m = m+str(s%3)
    s//=3
    print(s,m)

t =m.count('0')
print('yes',t)#99