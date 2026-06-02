n=int(input())
seg = []
for i in range(n):
    s,t= map(int, input().split())
    seg.append([s,t])
seg.sort()
left, right = 0,0
total = 0
for [s,t] in seg:
    if s <=right:
        right=max(right,t)
    else:
        total +=right-left
        left,right=s,t
total += right -left
print(total)