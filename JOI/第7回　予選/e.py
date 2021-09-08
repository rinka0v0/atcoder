# pypyならAC pythonだとTLE
r,c = map(int,input().split())
senbei = [list(map(int,input().split())) for i in range(r)]

row = [0 for i in range(r)]
for i in range(r):
    for j in range(c):
        row[i] += senbei[i][j]

backsum = 0
for i in row:
    backsum += c - i

maxinc = 0
for i in range(2**r):
    inc = 0
    rotate = []
    for j in range(r):
        if(i >> j) & 1 == 1:
            rotate.append(j)
    for j in rotate:
        inc += 2*row[j] - c
    for k in range(c):
        count = 0
        for l in range(r):
            if l in rotate:
                count += senbei[l][k] ^ 1
            else:
                count += senbei[l][k]
        if r < 2*count:
            inc += 2*count - r
    maxinc = max(maxinc,inc)

print(backsum + maxinc)