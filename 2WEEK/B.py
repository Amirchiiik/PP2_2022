a=input()
b=input().split()
b=list(map(int,b))
b.sort()
b.reverse()
print(b[0]*b[1])