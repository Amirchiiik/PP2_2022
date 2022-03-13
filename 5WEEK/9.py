import re
txt=input()
res=' '.join(re.findall('[A-Z][a-z]*',txt))
print(res)