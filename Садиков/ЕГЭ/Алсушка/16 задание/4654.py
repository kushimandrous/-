def f(n):
    print('начало',n)
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 1
    if n >3:
        print('больше 3',n)
        return f(n-3)+f(n-2)
print('результат',f(10))