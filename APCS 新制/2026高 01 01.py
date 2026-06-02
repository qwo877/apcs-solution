from functools import lru_cache

# 1. 讀取輸入
try:
    data = []
    while True:
        line = input().split()
        if not line: break
        data.extend(line)
except EOFError:
    pass


k = int(data[0])
idx = 1
all_letters = []
all_scores = []
initial_heights = []

for _ in range(k):
    n_i = int(data[idx])
    initial_heights.append(n_i)
    idx += 1
    
    # 存成「堆底到堆頂」方便索引
    letters, scores = [], []
    for _ in range(n_i):
        letters.append(data[idx])
        scores.append(int(data[idx+1]))
        idx += 2
    all_letters.append(letters[::-1])
    all_scores.append(scores[::-1])

# 2. 定義記憶化遞迴函數
@lru_cache(None)
def get_max_score(heights):
    max_s = 0
    # 嘗試所有可能的兩兩組合
    for i in range(k):
        if heights[i] == 0: continue
        for j in range(i + 1, k):
            if heights[j] == 0: continue
            
            # 檢查頂端字母是否相同
            if all_letters[i][heights[i]-1] == all_letters[j][heights[j]-1]:
                # 扣除高度，產生新狀態
                new_h = list(heights)
                new_h[i] -= 1
                new_h[j] -= 1
                
                # 計算分數：當前配對分數 + 剩餘狀態的最大分數
                gain = all_scores[i][heights[i]-1] + all_scores[j][heights[j]-1]
                max_s = max(max_s, gain + get_max_score(tuple(new_h)))
    
    return max_s

# 3. 執行並輸出結果
print(get_max_score(tuple(initial_heights)))


'''
你有k個堆疊,編號從1到k,每個堆過中包含若干個物品,每個物品有兩個屬性:
1. 一個大寫英文字母代表編號。
2.一個正整數代表分數。
你可以執行任意次操作直到無法操作為止:
操作:
1. 選擇兩個非空且不同的堆疊i和 j( 1 <= i ,j<= k equiv i ne j) 。
2. 檢查堆疊之和堆疊,頂部的物品。
3. 如果這兩個堆疊頂部物品的字母相同,則執行消除:
。從堆疊i和j中移除頂部物品。
。獲得的分數為這兩個被移除物品的分數總和。
4. 如果字母不同,則無法執行操作。
目標是執行一系列操作,使得你最終獲得的總分數最大。
'''