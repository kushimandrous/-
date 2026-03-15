with open("C:\\Users\\UserPC\\Desktop\\alsuege\\alsu\\9_27287 (1).csv") as f:
    c = 0
    for x in f:
        a = list(map(int,x.strip().split(';')))
        a.sort()
        dif = set(a)
        c = c + 1
        if len(dif)==3 and a[0] < a[1]:
            print(c,a[6])
