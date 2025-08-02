from collections import deque
n,p,l,r=map(int,input().split())
s=list(map(int,input().split()))
z=[False]*n
z[0]=True
q=deque()
q.append((0,0))
def a(n,p,l,r,s):
    while q:
        x ,y = q.popleft()
        if x==p:
            return y
        for dx in [-l,r]:
            nx=x+dx
            if 0<=nx<n:
                nx=s[nx]
                if 0<=nx<n and not z[nx]:
                    z[nx]=True
                    q.append((nx,y+1))
    return -1
print(a(n,p,l,r,s))