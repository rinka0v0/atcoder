H, W = map(int,input().split())

A = [list(map(int,input().split())) for i in range(H)]

B = [[0] * H for i in range(W)] 

for h in range(H):
    for w in range(W):
        B[w][h] = A[h][w]


for i in range(W):
    for j in range(H):
        print(B[i][j],end=' ')
    print()
