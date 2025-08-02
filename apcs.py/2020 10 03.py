m,n=map(int,input().split())
g=[list(map(int,input().split())) for _ in range(m)]
dp=[0]*n
l=[0]*n
r=[0]*n
l[0] = g[0][0]
for j in range(1, n):
    l[j] = max(g[0][j], l[j - 1] + g[0][j])
r[-1] = g[0][-1]
for j in range(n - 2, -1, -1):
    r[j] = max(g[0][j], r[j + 1] + g[0][j])

for j in range(n):
    dp[j] = max(l[j], r[j])
for i in range(1, m):
    l[0] = dp[0] + g[i][0]
    for j in range(1, n):
        l[j] = max(l[j - 1] + g[i][j], dp[j] + g[i][j])
    r[-1] = dp[-1] + g[i][-1]
    for j in range(n - 2, -1, -1):
        r[j] = max(r[j + 1] + g[i][j], dp[j] + g[i][j])
    for j in range(n):
        dp[j] = max(l[j], r[j])
print(max(dp))
