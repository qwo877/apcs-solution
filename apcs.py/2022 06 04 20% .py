def c(a, b, n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    pre = [[0] * (m + 1) for _ in range(n + 1)]
    ans = float('-inf')
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            dp[i][j] = a[i] * b[j]
            if n - i > 1 and m - j > 1:
                dp[i][j] = max(a[i] * b[j],max(dp[i+1][j+1],pre[i+1][j+1] + a[i] * b[j]))

            pre[i][j] = max(a[i] * b[j],pre[i+1][j+1] + a[i] * b[j])

            ans = max(ans, dp[i][j])

    return ans
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = c(a, b, n, m)
a.reverse()
ans = max(ans, c(a, b, n, m))
print(ans)