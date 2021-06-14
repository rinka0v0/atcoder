n = int(input())
s = input()

ans = 0

for i in range(1000):
    i = str(i).zfill(3)
    count1 = s.find(i[0])
    if count1 != -1:
        count2 = s.find(i[1],count1+1)
        if count2 != -1:
            count3 = s.find(i[2],count2+1)
            if count3 != -1:
                ans += 1

print(ans)
