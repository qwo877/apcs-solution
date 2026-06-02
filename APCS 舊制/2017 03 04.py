n,k=map(int,input().split())
p=list(map(int,input().split()))
p.sort()
def t(m):
    n=p[0]+m
    a=1
    for i in p:
        if i<=n: continue
        a+=1
        n=i+m
    return a<=k
l=0
r=(max(p)-min(p))
while r-l>1:
    mid=(l+r)//2
    if t(mid): r=mid
    else: l=mid
print(r)
