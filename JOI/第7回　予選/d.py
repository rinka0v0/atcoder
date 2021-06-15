import copy

m = int(input())
sign = list(list(map(int,input().split())) for i in range(m))
n = int(input())
photo = list(list(map(int,input().split())) for i in range(n))

x = sign[0][0]
y = sign[0][1]

for i in photo:
    vectorx = i[0] - x
    vectory = i[1] - y
    all = (copy.deepcopy(sign))
    count = True
    for j in range(m):
        all[j][0] = all[j][0] + vectorx
        all[j][1] = all[j][1] + vectory
        if all[j] not in photo:
            count = False
            break
    if count:
        print(vectorx,vectory)
    
    