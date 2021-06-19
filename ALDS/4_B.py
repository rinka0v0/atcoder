n = int(input())
s = list(map(int,input().split()))
q = int(input())
t = list(map(int,input().split()))

def isOk(index,key):
    if s[index] >= key:
        return True
    else:
        False

ans = 0

for i in t:
    left = -1
    right = n
    while right - left > 1:
        mid = right - (right - left)//2
        if(isOk(mid,i)):
            right = mid
        else:
            left = mid
    if s[right] == i:
        ans += 1

print(ans)
