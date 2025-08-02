from collections import deque
a = {"1B": 1, "2B": 2, "3B": 3, "HR": 4, "FO": 5, "GO": 5, "SO": 5}
b = [deque() for _ in range(11)]
base = deque([0, 0, 0])
cur_out, score = 0, 0
for i in range(9):
    l=list(input().split())
    n = int(l[0])  # 行為數
    for j in range(n):
        tmp = l[j+1]  # 行為名稱，例如 "1B"
        b[i].append(tmp)
out = int(input())

clear = False
cur_player = 0
while cur_out != out:
    if clear:
        base = deque([0, 0, 0])
        clear = False

    cmd = a[b[cur_player][0]]
    b[cur_player].popleft()    # 移除使用過的動作
    if cmd == 5:  # FO/GO/SO：出局
        cur_out += 1
        if cur_out % 3 == 0:
            clear = True
    else:
        # cmd = 1, 2, 3, 4（1壘~全壘打）
        base.append(1)  # 新打者上壘
        score += base.popleft()  # 本壘有人就得分
        for _ in range(cmd - 1):
            score += base.popleft()
            base.append(0)
    cur_player = (cur_player + 1) % 9
print(score)

            


