for a in range(100):
    b = True
    for x in range(100):
        if((x & a ==0) or (( x & 36 != 0 ) or (x & 6 != 0)))==0:
            
            b = False
    if b:
        print(a)