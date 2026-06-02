t=0
m=0
n,d=map(int,input().split())
for i in range(1,n+1):
  a,b,c=map(int,input().split())
  d1=abs(a-b)
  d2=abs(a-c)
  d3=abs(b-c)
  if d1>d-1 or d2>d-1 or d3>d-1:
    t=t+1
    m=m+(a+b+c)//3
print(t,m)