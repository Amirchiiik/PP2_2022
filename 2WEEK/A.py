def xxxtentacion(a):
    favor = len(a) - 1
    for i in range(len(a) - 2, -1, -1):
        if i + a[i]>=favor:
            favor = i
    return favor == 0
# 2 3 1 1 4
# 2 3 0 1 3 4 1 5 8 0 56 3 1
# 
a=list(map(int, input().split()))
b=xxxtentacion(a)
print(int(b))