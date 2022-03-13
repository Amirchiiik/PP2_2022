import re
a=input().split()
a=list(a)
x='a(b*)'
for i in a:
    if re.search(x,i):
        print(i)
