def isprime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
arr=[int(num) for num in input().split()]
filtered_arr=list(filter(lambda x:isprime(x),arr))
print(*filtered_arr)