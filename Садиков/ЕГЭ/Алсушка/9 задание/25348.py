with open("C:\\Users\\kushi\\Downloads\\9_25348.csv") as f:
    c = 0
    for p in f:
        a = list(map(int,p.strip().split(',')))
        a.sort()
        dif = set(a) #=5len
    
        if len(dif)==5:
            counts = [a.count(x) for x in dif]#проверяем что встрч 3 раза вложенным циклом
            if 3 in counts:
                mm = a[-1]
                if a.count(mm)==1:
                    c+=1
                    print(c)#1595