n = int(input())
location = [tuple(map(int,input().split())) for i in range(n)]
location_set = set(location)

ans = 0

for a in range(n):
    for b in range(n):
        ax,ay = location[a]
        bx,by = location[b]
        if ax == bx and ay < by:
            for i in range(n):
                cx,cy = location[i]
                if ax < cx and ay == cy:
                    if ((cx,ay) in location_set) and ((cx,by) in location_set):
                        ans += 1

print(ans)