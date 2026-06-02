n=int(input())
m=-1
e=0
tt=0
for i in range(n):
    t,s=map(int,input().split())
    if s==-1:
        e+=1
    elif s>m:
        tt=t
        m=s
ans=(m-n-(e*2))
if ans<0:
    ans=0
print(ans,tt)