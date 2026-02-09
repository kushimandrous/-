for x in range(2000):
    k = ""
    b = 0
    a = 3**100 - x
    while a > 0:
        k = k + str(a % 3)
        a = a // 3
    if k.count('0') == 2:
        print(x)
        