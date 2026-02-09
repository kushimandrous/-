for a in range(100,0,-1):
    b = True
    for x in range(100):
        if ((x & a == 0) or (x & 10 !=0) or (x & 3 !=0))==0:
            b = False 
    if b:
        print(a)
        break