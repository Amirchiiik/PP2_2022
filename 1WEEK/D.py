a=int(input())
b=input()
if b=='k': 
    c=int(input())
    k=float(a/1024)
    print(round(k,c))
else: 
    k=a*1024
    print(k)