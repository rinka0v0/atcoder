n = int(input())
H = list(map(int,input().split()))
ans = H[0]

for i in range(n - 1):
    if H[i] < H[i+1]:
        ans = H[i+1]
    else:
        break

print(ans)

