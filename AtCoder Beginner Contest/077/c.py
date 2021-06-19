
# AやCを固定して二分探索をするとTLEとなる。3層の構造になっている場合は中段を固定して考えると計算量が減る
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
a.sort()
b.sort()
c.sort()
ans = 0

def checkC(index,key):
    if c[index] > key:
        return True
    else:
        return False

def checkA(index,key):
    if a[index] < key:
        return True
    else:
        return False

for i in b:
    left = -1
    right = n
    while right - left > 1:
        mid = right - (right - left)//2
        if checkA(mid,i):
            left = mid
        else:
            right = mid
    if left == -1:
        continue
    else:
        indexa = left
        left = -1
        right = n
        while right - left > 1:
            mid = right - (right - left)//2
            if checkC(mid,i):
                right = mid
            else:
                left = mid
        if right == n:
            continue
        else:
            ans += (indexa + 1)*(n-right)

print(ans)