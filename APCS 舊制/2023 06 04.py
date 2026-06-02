from collections import deque
n,m,k=map(int,input().split())
t, *key = map(int, input().split())
vk=[[] for i in range(m)]
kg = [None] * n
nk=[k] * n
for i in range(n):
    a=list(map(int,input().split()))
    for j in a:
        vk[j].append(i)
for i in range(n):
        kg[i] = list(map(int,input().split()))
def f(a, q):
        for i in vk[a]:
            nk[i] -= 1
            if nk[i] == 0:
                q.append(i)
        vk[a].clear()

q = deque()
for i in key:
    f(i,q)
ans = 0
while q:
    box = q.popleft()
    ans += 1
    for i in kg[box]:
        f(i, q)
print(ans)
        
