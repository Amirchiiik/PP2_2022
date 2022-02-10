text=input()
text=text.split()
text=set(text)
a=[]
t=""
for i in text:
    for j in i:
        if j.isalpha():
            t+=j
    a.append(t)
    t=""
a.sort()
print(len(a))
for i in a:
    print(i)