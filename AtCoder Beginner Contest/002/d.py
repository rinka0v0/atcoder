n,m = map(int,input().split())

relationships = list(list(map(int,input().split())) for i in range(m))
ans = 0
for i in range(2**n):
    peoples = []
    count = True
    for j in range(n):
        if i >> j & 1 == 1:
            peoples.append(j+1)
    length = len(peoples)
    for x in range(length-1):
        for y in range(x+1,length):
            if [peoples[x],peoples[y]] not in relationships:
                count = False
    if count:
        ans = max(ans,length)
print(ans)