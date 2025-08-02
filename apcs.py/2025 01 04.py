from itertools import islice, accumulate
n, k = map(int,input().split())
mid = k //2
x = sorted(map(int,input().split()))
it = iter(x)
cur = -sum(islice(it, mid)) + sum(islice(it, k - mid))
if k & 1: cur -= x[mid]
dp = [cur]
for i in range(n - k):
    cur += x[i] - x[i + mid] + x[i + k] - x[i + k - mid]
    dp.append(cur)
print(min(map(int.__add__, accumulate(dp, min), dp[k:])))