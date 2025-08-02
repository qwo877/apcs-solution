from collections import deque
a = {"1B": 1, "2B": 2, "3B": 3, "HR": 4, "FO": 5, "GO": 5, "SO": 5}
b = [deque() for _ in range(11)]
base = deque([0, 0, 0])
cur_out, score = 0, 0
for i in range(9):
    l=list(input().split())
    n = int(l[0])
    for j in range(n):
        tmp = l[j+1]
        b[i].append(tmp)
out = int(input())

clear = False
cur_player = 0
while cur_out != out:
    if clear:
        base = deque([0, 0, 0])
        clear = False

    cmd = a[b[cur_player][0]]
    b[cur_player].popleft()
    if cmd == 5:
        cur_out += 1
        if cur_out % 3 == 0:
            clear = True
    else:
        base.append(1)
        score += base.popleft()
        for _ in range(cmd - 1):
            score += base.popleft()
            base.append(0)
    cur_player = (cur_player + 1) % 9
print(score)