for a in range(1,10000):
    for x in range (1,10000):
        if (not ( (x&28!=0) or (x&45!=0) )or ((not(x&17==0))or ( x&a!=0)))==1 :
            print(a)
    break