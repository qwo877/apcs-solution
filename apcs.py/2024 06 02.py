H,W,N = map(int,input().split())

a = [[0 for _ in range(W)] for _ in range(H)]
for _ in range(N):
    r,c,time,num = map(int,input().split())
    for rr in range(r - time,r + time + 1):
        for cc in range(c - time , c + time +1):
            if 0 <= rr < H and 0 <= cc < W and abs(rr - r)+ abs(cc-c) <= time: # 曼哈頓距離公式
                a[rr][cc] += num
for i in a:
    for j in i:
        print(j,end=' ')
    print('\n', end='')