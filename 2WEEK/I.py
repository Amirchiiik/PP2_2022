a=int(input())
cnt=0
d={}
s=[]
for i in range(a):
    name=input().split()
    name=list(name)
    if name[0]==1:
        d[name[0]]=name[1]
    print(d.keys())