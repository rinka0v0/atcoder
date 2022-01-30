s = input()
n = len(s)
 
ans = True
frontCount = 0
endCount = 0

for i in range(n):
    if s[i] == 'a':
        frontCount += 1
    else:
        break

if frontCount != len(s):
    for i in range(len(s) - 1, -1 , -1):
        if s[i] == 'a':
            endCount += 1
        else:
            break

    if endCount < frontCount:
        trimedS = s[endCount:n - endCount]
    else:
        trimedS = s[frontCount:n - endCount]
    trimedLen = len(trimedS)
    trimedMid = len(trimedS) // 2 + 1

    for i in range(trimedMid):
        if trimedS[i] != trimedS[trimedLen - 1 - i]:
            ans = False
            break

if ans:
    print('Yes') 
else:
    print('No')