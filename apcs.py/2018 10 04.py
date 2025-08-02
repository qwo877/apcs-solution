m, s, n = map(int, input().split())
x = list(map(int, input().split()))
t = sum(x)
tt = s - (m - t)

if tt <= 0:
    print(0)
else:
    max_sum = min(sum(x), 100000)
    dp = [False] * (m + 1)
    dp[0] = True

    for num in x:
        for j in range(m, num - 1, -1):
            if dp[j - num]:
                dp[j] = True

    for i in range(tt, m + 1):
        if dp[i]:
            print(i)
            break