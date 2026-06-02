def letterCase(c):
    if c.isupper():
        return 'u'
    if c.islower():
        return 'l'
    return 'n'

while True:
    try:
        k = int(input())
        g = 0      # 交錯字串最大長度
        cg = 0     # 目前交錯字串長度
        s = input()
        l = len(s)

        preL = 'n'    # 上一個字母是大寫u、小寫 l、未知n。
        curL = 'n'     # 目前字母是大寫u、小寫 l、未知n。
        ck = 0         # 目前字母case累積次數

        #  k 為 1 時要另外處理
        if(k == 1):
            for i in range(l):
                curL = letterCase(s[i])      # 取得字母大小寫
                if(preL != curL):    # 轉換大小寫時
                    cg = cg + 1
                else:                # 沒轉換大小寫時    
                    cg = 1
                g = max(cg, g)     # g 和 cg 誰是最大交錯字串長度
                preL = curL        # 上一個字母case為目前字母case
        else:
            for i in range(l):
                curL = letterCase(s[i])
                if preL == curL:
                    ck = ck + 1
                    if(ck == k):             # 累積到 k 次    
                        cg += k            # 加到目前交錯字串長度
                        g = max(cg, g)     # g 和 cg 誰是最大交錯字串長度

                    if(ck > k):              # 目前case次數超過 k 次
                            cg = k             # 目前交錯字串長度也只能等於 k
                    
                elif preL != curL:       # 轉換大小寫時
                    if ck < k:
                        cg = 0      # 目前case次數小於 k 次，目前交錯字串長度歸零
                    ck = 1                 # case次數從 1 開始
                preL = curL                # 上一個字母case為目前字母case

        print(g)
    except EOFError:
        break