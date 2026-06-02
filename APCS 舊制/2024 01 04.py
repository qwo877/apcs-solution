n = int(input())
a = list(map(int, input().split()))

b = [0] * (n + 1)
for i in range(1, n + 1):
    b[i] = b[i - 1] + a[i - 1]

def c(i, j):
    return b[j] - b[i - 1]

dp = [[0] * (n + 1) for _ in range(n + 1)]

for l in range(2, n + 1):
    for i in range(1, n - l + 2):
        j = i + l - 1
        dp[i][j] = float('inf')
        for k in range(i, j):
            cost = abs(c(i, k) - c(k + 1, j))
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + cost)

print(dp[1][n])