import sys
sys.setrecursionlimit(1000000)

n = int(input())
v = [[] for _ in range(n + 1)]
far = [0] * (n + 1)
st = set(range(1, n + 1))
ans = 0

for i in range(1, n + 1):
    tmp = list(map(int, input().split()))
    a = tmp[0]
    if a > 0:
        for b in tmp[1:]:
            v[i].append(b)
            if b in st:
                st.remove(b)
def dfs(id, dep):
    global ans
    if len(v[id]) == 0:
        far[id] = dep
        return
    for i in v[id]:
        dfs(i, dep + 1)
        far[id] = max(far[id], far[i])
    ans += far[id] - dep
root =st.pop()
dfs(root, 0)

print(root)
print(ans)