t =a= 0 
min=10*10
for i in range(1,10000):
    n = bin(i)[2:]# не работает не понимаю почему
    if i%2!=0:
        r = '0'+n+'1'
    else:
        r = n+bin(n.count('1'))[2:]
    if int(r,2)>250 and int(r,2)<min:
        a=i
        print(a)