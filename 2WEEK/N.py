a=[]
a2=[]
while 5>4:
    n1=int(input())
    if n1==0:
        break
    else:
        a.append(n1)
b=len(a)-1
if len(a)%2==0:
    for i in range(len(a)//2):
        a2.append(a[i]+a[b])
        b-=1
else:
    for i in range(len(a)//2+1):
        if i==len(a)//2:
            a2.append(a[i])
            continue
        a2.append(a[i]+a[b])
        b-=1
for i in a2:
    print(i,end=" ")


