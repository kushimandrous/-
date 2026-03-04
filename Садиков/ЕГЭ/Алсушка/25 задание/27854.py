def f(n):
    s = set()
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    s = sorted(s)
    return s 



for n in range(110203,110245+1):
    b = f(n)
    if b:
        r = [n for n in b if n%2==0]
        if r and len(r)==4:
            print(r)
 #[2, 4, 55102, 110204]
# [2, 14, 15746, 110222]
# [2, 6, 36742, 110226]
# [2, 22, 10022, 110242]

      
