def has33(arr):
    for i in range(len(arr)-1):
        if arr[i]=='3' and arr[i+1]=='3':
            return True  
        elif i==len(arr)-2:
            return False
n=input().split()
print(has33(n))