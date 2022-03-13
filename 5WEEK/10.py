#camel string to snake string HelloWorld->hello_world
import re
txt=input()
res='_'.join(re.findall('[A-Z][a-z]*',txt))
print(res.lower())