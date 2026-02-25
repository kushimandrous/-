s = '0123456789ab'
for x in s:
    d = '348'+x+'5'
    f = '1'+x+'111'
    c = int(d,11)+int(f,11)
    if c%8==0:
        print(c//8) #8292
