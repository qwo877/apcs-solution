from collections import deque

n,m=map(int,input().split())
a=[list(input()) for i in range(n)]
b= {'F': [(0, 1), (1, 0)],'H': [(0, -1), (0, 1)],'7': [(0, -1), (1, 0)],'I': [(-1, 0), (1, 0)],
    'X': [(-1, 0), (1, 0), (0, -1), (0, 1)],'L': [(0, 1), (-1, 0)],'J': [(0, -1), (-1, 0)]}
c= {
    (0, 1): (0, -1),
    (0, -1): (0, 1),
    (1, 0): (-1, 0),
    (-1, 0): (1, 0)
}
v=[[False]*m for i in range(n)]
ans=0
for i in range(n):
        for j in range(m):
            if v[i][j] or a[i][j] == '0':
                continue
            q = deque()
            q.append((i,j))
            v[i][j]=True
            size = 1
            while q:
                x, y = q.popleft()
                for dx, dy in b[a[x][y]]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        if not v[nx][ny] and a[nx][ny] != '0':
                             if c[(dx, dy)] in b[a[nx][ny]]:
                                v[nx][ny] = True
                                q.append((nx, ny))
                                size += 1
            ans = max(ans, size)
print(ans)