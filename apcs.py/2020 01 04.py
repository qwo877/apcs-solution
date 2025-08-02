n, m = map(int, input().split())
b = list(map(int, input().split()))
b = [0 for _ in range(n)] + b
c = list(map(int, input().split()))
tree = {}  # 記錄每個切換器的左右出口 (切換器或貨箱)
ll = {}  # 每個切換器左出口連到哪些貨箱（set）
rl = {}  # 每個切換器右出口連到哪些貨箱（set）
# 輸入每個切換器的左右出口
for _ in range(n - 1):
    p, s, t = map(int, input().split())
    tree[p] = (s, t)

# Tree 可以用 BFS 求出組拓樸順序
# 找到一個順序 [1 2 5 3 7 6 4 13 10 12 8 9 11]
# 只要 a->b 有一條邊，a 拓樸順序一定要在 b 前面

# 用 DFS 計算每個切換器的左右出口連到哪些貨箱
def dfs(node):
    if node >= n:
        # 是貨箱
        return b[node]
    l, r = tree[node]
    ls = dfs(l)
    rs = dfs(r)
    b[node] = ls + rs
    return b[node]
dfs(1)  # 從根節點 1 開始遞迴建立出口資訊
# 處理每個貨物
for w in c:
    curr = 1  # 從節點1開始

    while curr < n:
        b[curr] += w  # 更新該貨箱的重量
        l, r = tree[curr]
        ls = b[l]
        rs = b[r]
        if ls <= rs:
            curr = tree[curr][0]  # 往左
        else:
            curr = tree[curr][1]  # 往右
    print(curr, end=" ")
    b[curr] += w