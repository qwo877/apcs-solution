from itertools import chain, cycle
from sys import stdin
e=stdin.readline
m,n,k,i,j=map(int,e().split())
s=(-1,)
n+=1
l=list(chain.from_iterable(chain(map(int, e().split()), s) for _ in range(m)))
le=len(l)
i=i*n+j
r=cycle((1, n, -1, -n)).__next__
di=r()
ans=score=0
v=l[i]
while v!=0:
    score+=v
    ans+=1
    l[i]-=1
    if score%k==0:
        di=r()
    while 1:
        ni=i+di
        if 0<=ni<le:
            v=l[ni]
            if v!=-1:
                i=ni
                break
        di=r()
print(ans)