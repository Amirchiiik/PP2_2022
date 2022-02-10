date = input()
dates = []
while date != '0':
    date = date.split()
    date[2], date[0] = date[0], date[2]
    dates.append(date)
    date = input()
# for i in dates:
#     print(i)
dates.sort()
# print("--------------")
# for i in dates:
# #     print(i)
# print(dates[0][1])

for i in range(len(dates)):
    dates[i][0], dates[i][2] = dates[i][2], dates[i][0]
for i in dates:
    print(*i)
'''
11 09 0201
08 05 1945
23 10 1953
07 01 0001
12 12 2021
22 06 1941
21 12 2012
'''