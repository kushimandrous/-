s = 15**31+6*15**9+7*15**4+253
m=''
while s>0:
    m = m+str(s%15)
    s//=15
    print(s,m)

t =m.count('0')
print('yes',t) #26