x,n = map(int,input().split())
p =list(map(int,input().split()))
left = right = 0
for i in p:
    if i>x: right += 1
    else: left += 1
if right>left:
    print(right,max(p))
else:
    print(left,min(p))
