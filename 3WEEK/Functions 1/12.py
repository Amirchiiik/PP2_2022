a=input().split()
a=list(a)

for i in range(len(a)):
    for j in range(int(a[i])):
        print("*",end="")
    print()