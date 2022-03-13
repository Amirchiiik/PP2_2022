import re
txt=input()
res=re.search('^[A-Z]{1}[a-z]+$', txt)
print('the match is found' if res else 'Not found')