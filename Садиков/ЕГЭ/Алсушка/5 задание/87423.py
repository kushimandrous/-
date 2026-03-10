for n in range(10000, 1, -1):
    t = list(str(n))
    t = [int(i) for i in t if i != '0']
    p = 1
    for i in t:
        p *= i
    m = int(max(t)) - int(min(t))
    t1 = p + m
    t2 = p * m + 1
    r = str(min(t1,t2))+str(max(t1,t2))
    if r == '25127':
        print(n)
        break #9200