n = int(input())
coordinate = list(tuple(map(int,input().split())) for i in range(n))
set_coordinate = set(coordinate)

ans = 0

for i in range(n-1):
    nowx,nowy = coordinate[i]
    for j in range(i+1,n):
        nextx , nexty = coordinate[j][0],coordinate[j][1]
        vectorAx = nextx - nowx
        vectorAy = nexty - nowy
        vectorBx = -vectorAy
        vectorBy = vectorAx
        # リストに対してinは遅いためTLEとなってしまう
        if ((nowx + vectorBx,nowy + vectorBy) in set_coordinate) and ((nextx + vectorBx , nexty + vectorBy) in set_coordinate):
            ans = max((vectorAx**2 + vectorAy**2) , ans)

print(ans)
