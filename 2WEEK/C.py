a=int(input())
for i in range(a):
    for j in range(a):
        if i==j:
            print(i*j, end=" ")
        elif i==0:
            print(j, end=" ")
        elif j==0:
            print(i, end=" ")
        else: 
            print(0, end=" ")
    print()
