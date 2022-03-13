import re
txt=input()
res=re.search('[a-z]+_[a-z]+$', txt)
print('the match is found' if res else 'Not found')