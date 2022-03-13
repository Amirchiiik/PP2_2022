import re
txt=input()
res=re.search('^a{1}.+b{1}$', txt)
print('the match is found' if res else 'Not found')