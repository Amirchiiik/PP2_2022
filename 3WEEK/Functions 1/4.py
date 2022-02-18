def prime(n):
    if n==2:
        return True
    for i in range(3,n):
        if n%i==0:
            return False
    return True
def filter_prime(arr):
    filtered=[]
    for i in arr:
        if prime(i):
            filtered.append(i)
    return filtered
n=[int(num) for num in input().split()]
print(*filter_prime(n))