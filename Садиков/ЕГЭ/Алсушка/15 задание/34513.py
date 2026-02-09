for a in range(100):
    b = True
    for x in range(100):
        if((x&33 != 0)or not(x & 45 != 0) or (x & a != 0))==0:
            b = False
    if b:
        print(a)