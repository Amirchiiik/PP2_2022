a=input().split()
b=list(map(int,a))
if b[0]>500:
    print("Try next time!")
    exit()

for i in range(2, b[0]):
    if b[0]%i==0: 
        print("Try next time!")
        exit()

if b[1]%2==1: 
    print("Try next time!")
    exit()
    
print("Good job!")