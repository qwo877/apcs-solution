N,M,K=map(int, input().split())
a = list(range(1, N + 1))
k1 = 0
for _ in range(K):
    k1 = (k1 + M - 1) % len(a)
    e= a.pop(k1)
o = a[k1 % len(a)]
print(o)