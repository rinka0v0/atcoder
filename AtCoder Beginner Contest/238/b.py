n = int(input())
A = list(map(int,input().split()))

deg = 0
degs = []
degs.append(0)

ans = 0

for i in A:
    deg += i
    deg = deg % 360
    degs.append(deg)

degs.sort()
degs.append(360)

for i in range(n + 1):
    ans = max(degs[i + 1] - degs[i], ans)

print(ans)