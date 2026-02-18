from itertools import*
def f(x,y,z,w):
    return((w<=z)==(x<=(not(y)))) and (x or z)


for a1,a2 in product((0,1), repeat=2):
    s = [(1,0,0,1),(1,1,1,0,),(0,a1,0,a2)]
    if len(set(s))==3:
        for p in permutations ('xyzw'):
            if[f(**dict(zip(p,r))) for r in s]==[1,0,1]:
                print(p)
