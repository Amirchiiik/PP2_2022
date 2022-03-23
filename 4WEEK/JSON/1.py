import json
f=open('input.txt','r')
b=f.read()
cnt=0
dn=[]
speed=[]
mtu=[]
a=json.loads(b)
for i in a:
    if i=='imdata':
        for j in range(len(a[i])):
            for k in a[i][j]:
                for l in a[i][j][k]:
                    for s in a[i][j][k][l]:
                        if s=='dn':
                            dn.append(a[i][j][k][l][s])
                            cnt+=1
                        if s=='speed':
                            speed.append(a[i][j][k][l][s])
                            cnt+=1
                        if s=='mtu':
                            mtu.append(a[i][j][k][l][s])
                            cnt+=1 
                        # if cnt==9:
                        #     break
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  ------")
for i in range(len(dn)):
    print('{:<50} {:<20} {:<9} {:<30}'.format(dn[i], ' ', speed[i], mtu[i]) )

