s1 = input()
s2 = input()
s3 = input()
T = input()
ans = ''
for t in T:
    t = int(t)
    if t == 1:
        ans = ans + s1
    elif t == 2:
        ans = ans + s2
    else:
        ans = ans + s3
    
print(ans)

