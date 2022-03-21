a=input()
cnt1=0
cnt2=0
for i in a:
    if i==i.lower():
        cnt1+=1
    else: 
        cnt2+=1
print(f"Lower: {cnt1}\nUpper: {cnt2}")