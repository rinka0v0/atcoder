a,b,c,x,y = map(int,input().split())

ans = 10**5*500000

for i in range(max(x,y)+1):
    all = 2*c*i + a*max(0,x-i) + b*max(0,y-i)
    ans = min(ans,all)

print(ans)
