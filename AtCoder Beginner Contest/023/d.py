# ある値xが与えられた時x点以下となるように風船を割ることができるかを判定する。xは二分探索で探す。

n = int(input())
ballons = list(list(map(int,input().split())) for i in range(n))

def check(x):
    ls = []
    for i in range(n):
        if x <  ballons[i][0]:
            return False
        ls.append((x - ballons[i][0])//ballons[i][1])
    ls.sort()
    for i in range(n):
        if ls[i] < i:
            return False
    return True

left = -1
right = 10**12
while right - left > 1:
    mid = right - (right - left)//2
    if check(mid):
        right = mid
    else:
        left = mid

print(right)
