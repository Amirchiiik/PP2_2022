import re 
txt=input()
res=re.findall('[A-Z][a-z]*',txt)
print(res)