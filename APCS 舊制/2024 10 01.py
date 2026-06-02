p = int(input())
w1, w2, h1, h2 = map(int, input().split())
a = list(map(int, input().split()))
w1 = w1 * w1
w2 = w2 * w2
m = 1
ans = 0
for i in a:
    t = 0
    if m == 1:
        dh = i // w1
        if dh >= h1:
            i -= w1 * h1 
            t += h1
            m = 2 
        else:
            h1 -= dh
            t += dh
    if m == 2:
        dh = i // w2
        if dh >= h2:
            t += h2
            m = 3
        else:
            h2 -= dh
            t += dh
    if t > ans: 
        ans = t
    if m == 3: 
        break
print(ans)