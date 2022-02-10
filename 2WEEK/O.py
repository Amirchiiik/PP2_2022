import re
text=input()
text=text.replace('+',' ')
text=text.split()
fir=""
sec=""
thi=""
b=0
c=3
d={}
d['ONE']='1'
d['TWO']='2'
d['THR']='3'
d['FOU']='4'
d['FIV']='5'
d['SIX']='6'
d['SEV']='7'
d['EIG']='8'
d['NIN']='9'
d['ZER']='0'
while c!=len(text[0])+3:
    a=text[0][b:c]
    for key, value in d.items() :
        if a==key:
            fir+=value
            break
    b+=3
    c+=3
b=0
c=3
while c!=len(text[1])+3:
    a=text[1][b:c]
    for key, value in d.items() :
        if a==key:
            sec+=value
            break
    b+=3
    c+=3
e=int(fir)+int(sec)
for i in str(e):
    for key, value in d.items():
        if i==value:
            thi+=key
print(thi)
# ONETWOTHR+FOUFIVSIX


