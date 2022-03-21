import os
a=open('input.txt','r')
f=open('input1.txt','a')
for i in a:
    f.write(i)
a.close()
f.close()