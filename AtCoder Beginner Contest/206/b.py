n = int(input())
ans = 0
count = 0

i = 1
while ans < n:
    ans += i
    i += 1
    count += 1

print(count)