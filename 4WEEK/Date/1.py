from datetime import timedelta
import datetime

a=input().split("-")
a=list(a)
b=datetime.date(int(a[0]),int(a[1]),int(a[2]))
k = b - timedelta(days=5)
print('today:', b)
print('5 days ago:', k)