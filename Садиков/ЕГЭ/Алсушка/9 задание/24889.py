with open("C:\\Users\\kushi\\Downloads\\9_25348.csv") as f:
    c = 0
    for x in f:
        a = list(map(int,x.strip().split(',')))
        a.sort()
        dif = set(a)
        mini = a[0]
        maxi = a[-1]
        mc = a.count(maxi)
        if mc==3 or mc==4:
            un = []
            