x = 4**2015+2**2016-5
print ("Число х = ",x)
k = 0
t = ""
while x > 0:
    t = t + str(x % 2)
    if x % 2 == 1:
        k = k + 1
    x = x // 2
print("Счетчик числа 1 = ",k)
print("Результат t = ",t)
print(t.count('1'))