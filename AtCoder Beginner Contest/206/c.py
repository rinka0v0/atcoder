n = int(input())
a = list(map(int,input().split()))

a.sort()

def check(index,key):
    if key < a[index]:
        return True
    else:
        return False

ans = 0

for i in range(n):
    left = -1
    right = n
    while right - left > 1:
        mid = right - (right - left)//2
        if check(mid,a[i]):
            right = mid
        else:
            left = mid
    ans += n - right

print(ans)

