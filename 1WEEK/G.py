a=input()
k=len(a)-1
sum=0
for i in a:
    sum=(2**k)*int(i)+sum
    k=k-1
print(sum)
