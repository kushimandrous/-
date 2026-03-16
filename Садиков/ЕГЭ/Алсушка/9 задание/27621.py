with open("C:\\Users\\UserPC\\Desktop\\alsuege\\alsu\\9_27621.csv", encoding='utf-8-sig') as f: #Добавьте параметр encoding='utf-8-sig' в функцию open(). Это заставит Python автоматически игнорировать символы BOM.
    c = 0
    for x in f:
        a = list(map(int,x.strip().split(';')))
        a.sort()
        dif = set(a)
        mm = a[4]-a[0]
        ost = sum(a[1:4])
        c = c + 1
        if len(dif)==5 and mm==ost:
            print(c)
