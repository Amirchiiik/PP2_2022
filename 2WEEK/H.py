import math
a,b=input().split()
n=int(input())
s=[]
d={}
for i in range(n):
    x,y=input().split()
    f=math.sqrt((int(x)-int(a))**2+(int(y)-int(b))**2)
    s.append(f)
    d[f]=[x,y]
s.sort()
for i in s:
    print(*d[i])
