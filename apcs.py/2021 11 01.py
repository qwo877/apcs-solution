a=int(input())
b=list(map(int,input().split()))
c=0
for i in range(1,a-1):
    if b[i]==0:
        if b[i-1]>b[i+1]:
            c+=(b[i+1])
        else:
            c+=(b[i-1])
if b[0]==0:
    c+=(b[0+1])
if b[-1]==0:
    c+=(b[-1-1])
print(c)