mx=0
a = 0
for x in range(100,110):
    s = '1'*x
    while ('111'in s):
        s = s.replace('111','22',1)
        s = s.replace('222','11',1)
    if s.count('1')>mx:
            mx  = s.count('1')
            a = x
print(mx,a)


