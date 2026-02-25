from fnmatch import *

for i in range(0, 10 ** 10, 3013):
    d = str(i)
    if d[0] == '1':
        if fnmatch(d, '1?3948*5'):
            print(i)