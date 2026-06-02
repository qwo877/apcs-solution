import bisect

n, m = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
tp = sum(p)
a = [0]
for i in p:
    a.append(a[-1] + i)
b = a + [a[-1] + a[i] for i in range(1, n+1)]
pos = 0
s = 0
for i in q:
    c = i // tp
    d = i % tp
    s += c * n
    if d == 0:
        pass
    else:
        e = a[pos] + d
        idx = bisect.bisect_left(b, e, pos+1, pos+n+1)
        s += idx - pos
        pos = idx % n
ans = (s) % n
print(ans)