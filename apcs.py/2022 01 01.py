n,D=map(int,input().split())
s=list(map(int,input().split()))
win=0
x=s[0]
for i in range(1,len(s)):
  if x==0:
    if s[i]<=(last-D):
      x=s[i]
  else:
    if s[i]>=(x+D):
      win+=(s[i]-x)
      last=s[i]
      x=0
print(win)