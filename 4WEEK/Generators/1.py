def gen(n):
    for i in range(n):
        b=i**2
        yield b

n=int(input())
s=list(gen(n))
print(s)

