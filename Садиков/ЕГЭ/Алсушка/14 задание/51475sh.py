s = 6*343**6+5*49**7-40
m = ''
while s>0:
    m = m + str(s%7)
    s//=7
    print(s,m)

t =m.count('6')
print('yess',t) #13