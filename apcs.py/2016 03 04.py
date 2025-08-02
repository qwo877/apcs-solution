from collections import deque, defaultdict
n=int(input())
g=defaultdict(list)#紀錄圖表
for _ in range(n - 1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
def bfs(s):
    v= set()#訪問過了
    q = deque()#代訪問列表
    q.append((s, 0))#訪問初值(防止while無法執行)
    v.add(s)#訪問過初值了
    ans=0#訪問距離
    m=s#最遠點
    while q:#進行BFS
        x,y=q.popleft()
        if y>ans:
            ans = y
            m=x
        for i in g[x]:
            if i not in v:
                v.add(i)
                q.append((i, y + 1))
    return m, ans
a,_=bfs(0)
b,ans=bfs(a)
print(ans)

