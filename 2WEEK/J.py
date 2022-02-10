n1=int(input())
a=[]
low=0
upp=0
num=0
for i in range(n1):
    pas=input()
    for i in pas:
        if ord(i)>=97 and ord(i)<=122:
            low+=1
        elif ord(i)>=65 and ord(i)<=95:
            upp+=1
        elif ord(i)>=48 and ord(i)<=57:
            num+=1
    if low!=0 and upp!=0 and num!=0:
        if pas not in a:
            a.append(pas)
    low=0
    upp=0
    num=0
print(len(a))
a.sort()
for i in a:
    print(i)