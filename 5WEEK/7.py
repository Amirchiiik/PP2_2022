import string 
import re
txt=input()  
new_str=""
for i in range(len(txt)):
    if i==0:
        new_str+=txt[i].upper()
    elif txt[i]=='_':
        new_str+=txt[i+1].upper()
    elif txt[i-1]=='_':
        continue
    else:
        new_str+=txt[i]
print(new_str)