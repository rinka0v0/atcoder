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
    
    

# 2回目解いた時のコード
m = int(input())
signs = [list(map(int,input().split())) for i in range(m)]
n = int(input())
specimen = [tuple(map(int,input().split())) for i in range(n)]
set_specimen = set(specimen)
nowx = signs[0][0]
nowy = signs[0][1]

for i in range(n):
    dx = specimen[i][0] - nowx
    dy = specimen[i][1] - nowy
    for j in range(m):
        if not((signs[j][0] + dx,signs[j][1] + dy) in set_specimen):
            break
        if j == m-1:
            print(dx,dy)