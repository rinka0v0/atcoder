n,m = map(int,input().split())
switchNumber = []
bulb = []
ans = 0

for i in range(m):
    l = list(map(int,input().split()))
    switchNumber.append(l[0])
    switch= l[1:]
    bulb.append(switch)
p = list(map(int,input().split()))

n,m = map(int,input().split())
switchNumber = []
bulb = []
ans = 0

for i in range(m):
    l = list(map(int,input().split()))
    switchNumber.append(l[0])
    switch= l[1:]
    bulb.append(switch)
p = list(map(int,input().split()))
# print(bulb)
# print(switchNumber)

for i in range(2**n):
    a = True
    # print(i,'i')
    for j in range(m):
        count = 0
        # print(j,'j')
        for k in range(switchNumber[j]):
            # print(k,'k')
            # print(bulb[j][k],'bulb[j][k]')
            count +=  i >> (bulb[j][k] -1) & 1 
        if count%2 != p[j]:
            a = False
            break
    if a :
        ans += 1

print(ans)