s = '7'*16+'3'*1600+'8'*8
while ('7'in s) or ('33'in s) or ('888' in s):
    if '7'in s:
        s=s.replace('7','33',1)
    elif '33' in s:
        s=s.replace('33','3',1)
    elif '888' in s:
        s=s.replace('888','7',1)
print(s)