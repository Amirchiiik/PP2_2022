import string
def palindrom(s):
    news=""
    for i in range(len(s)-1,-1,-1):
        news+=s[i]
    if news==s:
        return "Yes"
    else:
        return "No"
n=input()
print(palindrom(n))

