for x in '0123456789abcdef':
    s = '2' + x + '84'
    m = '2' + 'b' + '3' + x + ''
    r = int(s,19) + int(m,16)
    if r %88 == 0:
        print(r // 88)

