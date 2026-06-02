n,m = map(int,input().split())
mat = []
for i in range(n):
    mat.append([int(x) for x in input().split()])
    
point = [] # answer
for i in range(n):
    for j in range(m):
        x = mat[i][j]
        total = 0
        #enumerate all (s,t) in range
        for s in range(i-x,i+x+1):
            for t in range(j-x,j+x+1):
                if 0<=s<n and 0<=t<m and abs(i-s)+abs(j-t)<=x:
                    total += mat[s][t]
        if (total-x)%10==0:
            point.append((i,j))
# output answer
print(len(point))
for r,c in point:
    print(r,c)
