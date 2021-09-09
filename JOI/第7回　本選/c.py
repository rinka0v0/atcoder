# 半分全列挙＆2分探索
n , m = map(int,input().split())
p = [int(input()) for i in range(n)]
p = sorted(p)
p.append(0)
s = []
for p1 in p:
    for p2 in p:
        s.append(p1 + p2)
s = sorted(s)

def isOk(index,value):
    if s[index] > value:
        return True
    else:
        return False

ans = 0

for i in s:
    if m < i:
        break
    right = n**2 + 2*n + 1
    left = -1
    while right - left > 1:
        mid = (right + left) // 2
        if isOk(mid,m-i):
            right = mid
        else:
            left = mid
    if left == -1:
        ans = max(ans,i)
    else:
        ans = max(ans,(i + s[left]))

print(ans)
    