import sys
input = sys.stdin.read
data = input().split()
    
n = int(data[0])
pre = float('inf')
ans = 0
cnt = 0
for i in range(1, n + 1):
    x = int(data[i])
    if x >= pre:
        cnt = 0
    cnt += 1
    ans = max(ans, cnt)
    pre = x
print(ans)