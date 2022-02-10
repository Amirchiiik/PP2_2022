s=str(input())
ar=[]
for i in range(len(s)):
    if s[i]=='(' or s[i]=='{' or s[i]=='[':
        ar.append(s[i])
    elif s[i]==')':
        if len(ar)==0:
            print("No")
            exit()
        elif ar[-1]=='(':
            ar.pop()
        else:
            print("No")
            exit()
    elif s[i]=='}':
        if len(ar)==0:
            print("No")
            exit()
        elif ar[-1]=='{':
            ar.pop()
        else:
            print("No")
            exit()
    elif s[i]==']':
        if len(ar)==0:
            print("No")
            exit()
        elif ar[-1]=='[':
            ar.pop()
        else:
            print("No")
            exit()
if len(ar)==0:
    print("Yes")
else:
    print("No")