cnt=0
sum=0
a=input()
for i in a:
    sum=sum+ord(a[cnt])
    cnt=cnt+1
if sum>300: 
    print("It is tasty!")
else: print("Oh, no!")