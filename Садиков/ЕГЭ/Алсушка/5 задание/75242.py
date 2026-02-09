for n in range(1864245, 10**10):
    s = ''
    while n > 0:
        s += str(n%3)
        n //= 3
    s = s[::-1]
    R = s.replace('0','*').replace('2','0').replace('*','2')
    if abs(int(s,3) - int(R,3)) == 1864246:
        print(int(s,3))
        break