import os
a=input().split()
a=list(a)
f=open('input.txt','a')
for i in a:
    f.write("%s\n" % i)
f.close()
f=open('input.txt','r')
print(f.read())