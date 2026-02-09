for i in range(1,260):
    n=bin(i)[2:]
    if i%2==0:
        n = n+'01'
    else:
        n = '0'+ n+'11'
    r = int(n,2)
    if r>1021:
        print(i)