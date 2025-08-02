from collections import deque
n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
d=[(1,0),(-1,0),(0,1),(0,-1)]
l,r=0,max(max(row) for row in a) - min(min(row) for row in a)
ans=r
def c(mid):
    b=[[False]*n for i in range(n)]
    q =deque()
    q.append((0,0,))
    b[0][0]=True
    while q:
        x,y=q.popleft()
        if x==n-1 and y==n-1:
            return True
        for dx ,dy in d:
            nx ,ny = x+dx,y+dy
            if 0<=nx <n and 0<=ny <n and not b[nx][ny]:
                if abs(a[nx][ny]-a[x][y])<=mid:
                    b[nx][ny]=True
                    q.append((nx,ny))
    return False
                    
def e(ans):
    dist=[[-1]*n for i in range(n)]
    q=deque()
    q.append((0,0))
    dist[0][0]=0
    while q:
        x,y=q.popleft()
        if x==n-1 and y==n-1:
            return dist[x][y]
        for dx ,dy in d:
            nx ,ny = x+dx,y+dy
            if 0<=nx <n and 0<=ny <n and dist[nx][ny]==-1:
                if abs(a[nx][ny] - a[x][y]) <= ans:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))

    return -1
                
            
while l<=r:
    mid=(l+r)//2
    if c(mid):
        ans=mid
        r=mid-1
    else:
        l=mid+1
ans2=e(ans)
print(ans)
print(ans2)
