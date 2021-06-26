l= list(map(int,input().split()))

ans = max((l[0]+l[1]),(l[0]+l[2]),(l[1]+l[2]))

print(ans)