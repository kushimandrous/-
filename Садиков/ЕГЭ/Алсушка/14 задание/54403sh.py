s = '0123456789abcdefghijklm'
for x in s:
    d = '14'+x+'d'
    f = 'a'+x+'f111'
    v = int(d,23)+int(f,23)
    if v%17==0:
        print(v//17) #4044632