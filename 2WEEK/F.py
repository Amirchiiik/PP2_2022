money={}
a=int(input())
for i in range(a):
    name, point = input().split()
    if name not in money.keys(): 
        money[name] = 0
    money[name] += int(point)
max_val = max(money, key=money.get)
s=list(money.keys())
s.sort()
for i in s:
    if money[i]==money[max_val]:
        print(i+" is lucky!")
    else:
        print(i+" has to receive "+ str(int(money[max_val])-int(money[i]))+" tenge")
    