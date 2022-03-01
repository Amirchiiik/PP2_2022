from datetime import timedelta
import datetime

a=input().split("-")
b=input().split("-")
a=list(a)
b=list(b)
a=datetime.date(int(a[0]),int(a[1]),int(a[2]))
b=datetime.date(int(b[0]),int(b[1]),int(b[2]))
sec = a - b
print(sec.days*24*60*60, "sec")