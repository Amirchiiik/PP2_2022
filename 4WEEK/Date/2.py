from datetime import timedelta
import datetime

a=input().split("-")
a=list(a)
b=datetime.date(int(a[0]),int(a[1]),int(a[2]))
yesterday = b - timedelta(days=1)
tomorrow = b + timedelta(days=1)
print('yesterday:', yesterday)
print('today:', b)
print('tomorrow', tomorrow)
