n,m=map(int,input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ans = float('inf')
for i in range(n):
    for j in range(m):
        if a[i][j] < ans:
            ans = a[i][j]
            x,y=i,j
v = [[False]*m for i in range(n)]
v[x][y]=True
f = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while 1:
    d=float('inf')
    e= None
    for dx, dy in f:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not v[nx][ny]:
            if a[nx][ny] < d:
                d = a[nx][ny]
                e = (nx, ny)
    if e is None:
        break
    x,y=e
    ans+=a[x][y]
    v[x][y]=True
    
print(ans)