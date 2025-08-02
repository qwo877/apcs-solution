from collections import deque, defaultdict

p, q, r, m = map(int, input().split())                
ui = list(map(int, input().split()))
ti = list(map(int, input().split()))
mi = []
for i in range(m):
    a, b = map(int, input().split())
    mi.append((a, b))
n = p + q + r
a = [0] * (n + 1) # 邏輯值
b = [0] * (n + 1) # 最大延遲時間
c = [0] * (n + 1)  # 入度(拓樸)
adj = [[] for _ in range(n + 1)]# 鄰接
iv = defaultdict(list)#輸入值

for i in range(p):
    a[i + 1] = ui[i]

for u, v in mi:
    adj[u].append(v)
    c[v] += 1

q_ = deque()
for i in range(1, p + 1):
    q_.append(i)

while q_:
    u = q_.popleft()
    for v in adj[u]:
        iv[v].append(a[u])
        c[v] -= 1
        b[v] = max(b[v], b[u] + 1)
        if c[v] == 0:
            if p + 1 <= v <= p + q:
                gt = ti[v - p - 1]
                ins = iv[v]
                if gt == 1:
                    a[v] = ins[0] & ins[1]
                elif gt == 2:
                    a[v] = ins[0] | ins[1]
                elif gt == 3:
                    a[v] = ins[0] ^ ins[1]
                elif gt == 4:
                    a[v] = 1 - ins[0]
            else:
                a[v] = iv[v][0]
            q_.append(v)
ans = []
md = 0
for i in range(p + q + 1, p + q + r + 1):
    ans.append(a[i])
    md = max(md, b[i])
print((md-1))
print(*ans)