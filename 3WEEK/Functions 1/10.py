def unique(arr):
    d={}
    new_arr=[]
    for i in range(len(arr)):
        if arr[i] in d:
            d[arr[i]]+=1
        else:
            d[arr[i]]=1
    for i in d:
        if d[i]==1:
            new_arr.append(i)
    return new_arr
n=[int(num) for num in input().split()]
print(*(unique(n)))