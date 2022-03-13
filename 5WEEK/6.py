import re
txt=input()
res=re.sub('\W',':',txt)
print(res)
