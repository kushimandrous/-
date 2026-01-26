x = 9**18+3**54-9
k = 0
while x>0:
    if x%3 == 2:
        k = k+1
    x = x//3
print(k)
