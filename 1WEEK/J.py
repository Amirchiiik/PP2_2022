a=input()
k=[]
sum=''
cnt=0
for i in a: 
    if i!=' ':
        sum=sum+i
    if i==' ' or cnt==len(a)-1:
        if len(sum)>=3:
            print(sum,end=' ')
        sum=''
    cnt+=1

