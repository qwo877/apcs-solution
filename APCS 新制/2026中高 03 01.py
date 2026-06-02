n, m = map(int, input().split())

w = [0] + [int(x) for x in input().split()]
    
P = [0] * (n + 1)
for i in range(1, n + 1):
        P[i] = P[i - 1] + w[i]

for _ in range(m):
    l,r,a,b = map(int, input().split())
        
        # 整個區間 [l, r] 的總和 S(l, r)
    S = P[r] - P[l - 1]
        
        # 預先計算條件中需要的值
    q = a * S
    e = a + b
        
    ll = l #二分裸題 所以二分範圍直接就是 l 到 r
    rr = r
    ans = r
        
    while ll <= rr: #使用小於等於的原因是當 low == high 時，mid 仍然會等於 low (或 high)，這時候我們還是需要檢查這個位置是否滿足條件
        mid = (ll + rr) // 2
            # 計算 S(l, mid) SS:詢問中的區間總合
        SS = P[mid] - P[l - 1] #l-1 是因為 P 是從 1 開始的前綴和陣列，P[i] 包含了 w[1] 到 w[i] 的總和，所以要計算 S(l, mid) 就是 P[mid] - P[l-1]，這樣就能得到從 l 到 mid 的總和。
            
            # 判斷S(l, k) * (a + b) >= a * S(l, r)
        if SS * e >= q:
            ans = mid       # 找到一個滿足條件的 k，先暫存起來
            rr = mid - 1  # 試著往左邊找看看有沒有更小的 k
        else:
            ll = mid + 1   # 總和不夠大，必須往右邊找
                
    print(ans)