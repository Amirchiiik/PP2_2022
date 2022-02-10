a=input().split()
a=list(a)
if len(a)<=1:
    b=int(input())
    temp=0
    for i in range(int(a[0])):
        temp^=b+2*i
    print(temp)
else:
    temp=0
    for i in range(int(a[0])):
        temp^=int(a[1])+2*i
    print(temp)


