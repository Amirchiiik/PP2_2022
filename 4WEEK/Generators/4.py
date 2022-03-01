def squares(a,b):
    for i in range(a,b):
        c=i**2
        yield c

a=int(input())
b=int(input())
for i in squares(a,b):
    print(i,end=" ")

