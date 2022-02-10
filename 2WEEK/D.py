a=int(input())
for i in range(a):
    for j in range(a):
        if a%2==1:
            if i+j>=a-1:
                print("#", end="")
            else:
                print(".", end="")
        else:
            if i>=j:
                print("#", end="")
            else:
                print(".", end="") 
    print()