strng = '1' * 104
while ('111' in strng):
    strng = strng.replace('111', '22', 1)
    strng = strng.replace('222', '11', 1)
print(strng)