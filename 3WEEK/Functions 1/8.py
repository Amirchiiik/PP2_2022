def spygame(a):
    cnt1=0
    f=[]
    for i in range(len(a)):
        if a[i]=='0' or a[i]=='7':
            f.append(a[i])
    newstr=""
    for i in f:
        newstr+=i
    if "007" in newstr:
        return True
    else: 
        return False
n=input().split()
print(spygame(n))