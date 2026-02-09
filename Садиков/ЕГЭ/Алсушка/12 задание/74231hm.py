s = '3'*20+'6'*26+'9'*31
c=0
while ('36'in s) or ('63'in s) or ('69'in s):
    if '69'in s:
        s=s.replace('69','63',1)
        c+=1
    if '36' in s:
        s =s.replace('36','3',1)
        c+=1
    if '63'in s:
        s=s.replace('63','9',1)
        c+=1
print(c)
