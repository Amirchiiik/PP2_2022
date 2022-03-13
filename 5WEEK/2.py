import re
a=input().split()
a=list(a)
x='ab{2,3}'
for i in a:
    if re.search(x,i):
        print(i)
