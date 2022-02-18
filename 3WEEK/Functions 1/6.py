def reverse(arr):
    reverse_str=[]
    for i in range(len(arr)-1,-1,-1):
        reverse_str.append(arr[i])
    return reverse_str
n=input().split()
for i in reverse(n):
    print(i,end=' ')