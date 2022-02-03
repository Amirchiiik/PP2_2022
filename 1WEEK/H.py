s=input()
k=input()
cnt=0
ff=[]

for i in s:
    if i==k:
        ff.append(cnt)
    cnt=cnt+1
if len(ff)==1:
    print(ff[0])
else:
    print(ff[0],ff[len(ff)-1])
