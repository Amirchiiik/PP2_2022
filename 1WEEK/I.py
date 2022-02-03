s=int(input())
for i in range(s):
    k=input()
    if k.find('@gmail.com')>=0:
        b=k.replace('@gmail.com','')
        print(b)

