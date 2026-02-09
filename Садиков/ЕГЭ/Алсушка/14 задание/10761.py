for x in'0123456789ABCDEF':
    m = int('135' + x + 'F',16)
    n = int('9' + x + '531',16)
    if (m + n) % 8 == 0:
        print((m + n) // 8)