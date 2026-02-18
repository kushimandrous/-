# for x in range(53671,125699):
#     c = set()
#     if x**0.5==int(x**0.5):
#         for i in range(1,int(x**0.5) +1):
#             if x%i ==0:
#                 c.add(i)
#                 c.add(x//i)
#     if len(c)==5:
#         print(x)
#83521 - ответ


# def prime(x):
#     for i in range(2,int(x**0.5)+1):
#         if x%i == 0:
#             return False
#     return x!=1  #функция на простые числа 


# c = []


# for x in range(182635,453734):
#     f = 0
#     for i in range(2,int(x**0.5)+1):
#         if (x%i==0) and prime(i) and prime(x//i) and (i!=x//i):
#             f = 1
#             break
#     if f ==1:
#         c.append(x)
# print(len(c),max(c)+min(c))# 57221 636366 ответ



# def prime(x):
#     for i in range(2,int(x**0.5)+1):
#         if x%i == 0:
#             return False
#     return x>1  #функция на простые числа 


# m=[]
# for x in  range(500001,535243):
#     c = set()
#     for i in range(2,int(x**0.5)+1):
#         if x%i==0:
#             c.add(i)
#             c.add(x//i)
#     sm = sum(c)
#     if (sm % 184 ==0) and(prime(sum(int(i) for i in str(sm)))):
#         m.append(x)
# print(min(m)) #500191


# for x in range(800000,999000):
#     cc =set()
#     cn = set()
#     for i in range(2,int(x**0.5)+1):
#         if x%i ==0:
#             if i%2 == 0:
#                 cc.add(i)
#             else:
#                 cn.add(i)
#             if x//i  %2 == 0:
#                 cc.add(x//i)
#             else:
#                 cn.add(x//i)
#     if sum(cn)%2==0 and sum(cc) % 10 == 4:
#         print(x,len(cn)+len(cc))#806450 16
# 814088 34
# 816642 28
# 819200 46
# 821762 4 это все ответ типо 










