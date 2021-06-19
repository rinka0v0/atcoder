d = int(input())
n = int(input())
m = int(input())
stores  = list(int(input()) for i in range(n-1))
customers = list(int(input()) for i in range(m))
stores = sorted(stores)
ans = 0

def isOk(index,key):
    if(stores[index] >= key):
        return True
    else:
        return False

for customer in customers:
    left = -1
    right = n -1
    while right - left > 1:
        mid = right - (right - left)//2
        if(isOk(mid,customer)):
            right = mid
        else:
            left = mid 
             
    if left == -1:
        ans += min(abs(stores[right]-customer),customer)
    elif right == n-1:
        ans += min(abs(stores[left]-customer),(d-customer)) 
    else:
        ans += min(abs(stores[right] - customer),abs(stores[left] - customer))
    
print(ans)
           
