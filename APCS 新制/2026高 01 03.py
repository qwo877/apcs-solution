import sys
input = sys.stdin.readline

n = int(input())
P = list(map(int, input().split()))

#紀錄每個數值的索引位置
pos = [0] * (n + 1)
for i in range(n):
    pos[P[i]] = i

#Fenwick Tree: 初始化為 1，表示位置 i 還有元素擋路
tree = [0] * (n + 1)
def update(i, delta):
    i += 1 # 轉為 1-based
    while i <= n: #這裡的n是第28行的n，代表元素總數
        tree[i] += delta
        i += i & -i

def query(i):
    i += 1
    s = 0
    while i > 0:
        s += tree[i]
        i -= i & -i
    return s

for i in range(n):
    update(i, 1)

#追蹤「目標值」
需要額外pop的次數 = 0
指針目前停在哪個位置 = -1 # 從最左邊開始

for v in range(1, n + 1):
    要找到哪裡 = pos[v]
    
    # 計算 指針目前停在哪個位置 到 要找到哪裡 之間有多少需要額外pop的元素
    if 要找到哪裡 > 指針目前停在哪個位置:
        # -1 是因為 query 是 inclusive 的，所以要找到哪裡 - 1 才是正確的範圍
        count = query(要找到哪裡 - 1) - query(指針目前停在哪個位置)
    else:
        # 如果要找到哪裡 在指針目前停在哪個位置的左邊，則需要額外pop的元素是從指針目前停在哪個位置 到 要找到哪裡 之間的元素數量
        count = query(指針目前停在哪個位置 - 1) - query(要找到哪裡)
    
    需要額外pop的次數 += max(0, count)
    
    # 輸出 v，把 target_idx 標記為已移除 (delta = -1)
    update(要找到哪裡, -1) #要在做一次更新是因為要把已經找到的元素從Fenwick Tree中移除
    指針目前停在哪個位置 = 要找到哪裡

print(n + 需要額外pop的次數)


'''
給定一個長度為的排列(Permutation) P (P1, P2,..., Pn),包含從1到的所有整數。一開始,所有元素都按照它們在P中的順序,從pm到P1 依次被壓入 Stack S2 中
(即P在底,P1在頂)。
目標是要透過這兩個stack的 push 和 pop 操作來將這個排列做由小到大排序,並且輸出最少需要多少 pop 操作。
'''