def f(x):
  global ans, idx
  n = 2+(x%2)
  for i in range(n):
    idx += 1
    nxt = a[idx]
    if nxt == 0:
      continue
    ans += abs(x-nxt)
    f(nxt)

a = list(map(int, input().split()))
ans = 0
idx = 0
f(a[idx])
print(ans)