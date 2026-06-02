def main():
    from sys import stdin
    from itertools import permutations
    e = stdin.readline

    n = int(e())
    s = [0] * n
    d = [0] * n
    t = [0] * n
    for i in range(n):
        s[i], d[i], t[i] = map(int, e().split())
    lim = max(d)

    def check(x):
        end = -x #初始時間為 -x，因為第一個任務開始前的休息時間也是算在內的
        for i in p:
            end = max(end + x, s[i]) + t[i] #每個任務的開始時間至少是前一個任務結束時間 + 休息時間，或者是任務本身的開始時間 s[i]，取兩者的較大值，再加上任務的處理時間 t[i]
            if end > d[i]: return False #如果任務的結束時間超過了截止時間 d[i]，就表示這個休息時間 x 不可行，返回 False
        return True

    ans = 0
    for p in permutations(range(n)): #枚舉所有任務的執行順序 並且二分搜尋休息時間 並以 check 函數驗證是否可行
        if not check(ans): continue #如果目前的休息時間 ans 不可行 就跳過這個任務順序
        lo, hi = ans, lim # 休息時間不可能超過 lim，因為任務最晚在 lim 時完成
        while lo < hi: 
            mid = lo + hi >> 1
            if check(mid): #如果 mid 這個休息時間可行 就嘗試更大的休息時間
                lo = mid + 1
            else: #如果 mid 這個休息時間不可行 就嘗試更小的休息時間
                hi = mid
        if lo > ans:  #如果這個任務順序的最大休息時間 lo 比目前的 ans 還大 就更新 ans
            ans = lo - 1 #因為 lo 是第一個不可行的休息時間，所以真正可行的最大休息時間是 lo - 1
    print(ans)
main()

'''
你擁有一台印刷機,需要處理個印刷任務。每個印刷任務都有三個相關的參數:
1. 開始時間 (Start Time, si):任務,可以在si或之後開始印刷。
2. 截止時間 (Deadline, d₁):任務必須在di或之前完成印刷。
3. 所需時間 (Processing Time, t₁): 任務需要秒的連續時間來完成印刷。
印刷機在某一秒完成一個印刷品後,可以在下一秒開始時立即開始列印下一個印刷品。
我們希望排定這個印刷任務的執行順序,使得所有任務都能在其截止時間內完成。然而若是讓印刷機空閒時間不足會減損印刷機的壽命,為了維護印刷機的壽命,我們希望最大
化印刷機在能夠執行全部任務的前提下,任兩個任務的間隔時間最大值。
任兩個任務的間隔時間定義為:在完成前一個印刷任務與開始下一個印刷任務之間,印刷機閒置的時間長度。
你的任務是找出一個有效的任務排程順序,使得所有任務都能在截止時間內完成,並且印刷機在整個排程中獲得的總休息時間最大。
'''