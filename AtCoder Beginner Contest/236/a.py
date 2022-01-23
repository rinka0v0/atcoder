s = input()
a,b = map(int,input().split())

x = s[a - 1]
y = s[b - 1]
ans = s[:a - 1] + y + s[a:b - 1] + x + s[b:]
print(ans)
