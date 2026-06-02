n,m=map(int,input().split())
ds=[[-1]]+[[-1,3,5,1,2,6,4] for _ in range(n)]
def top(d):
    return d[3]
def front(d):
    d[1],d[3],d[6],d[5]=d[5],d[1],d[3],d[6]
def right(d):
    d[2],d[3],d[4],d[5]=d[5],d[2],d[3],d[4]
for i in range(m):
    a,b=map(int,input().split())
    if b>0: ds[a],ds[b]=ds[b],ds[a]#swap(s[a],s[b])
    elif b==-1: front(ds[a])
    elif b==-2: right(ds[a])
for i in range(1,n+1):
    print(top(ds[i]),end=' ')
