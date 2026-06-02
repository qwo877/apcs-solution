m,n = [int(t) for t in input().split()]
mat = []
for i in range(m):
    mat.append([int(t) for t in input().split()]+[1001])
mat.append([1001]*n)
ans = 0
modified = True
while modified:
    modified = False
    for r in range(m):
        for c in range(n):
            if mat[r][c]<0: continue 
            i = r+1
            while mat[i][c]<0: i += 1
            if mat[r][c] == mat[i][c]:
                ans += mat[r][c]
                mat[r][c]=mat[i][c]=-1
                modified = True
                continue
            j = c+1
            while mat[r][j]<0: j += 1
            if mat[r][c] == mat[r][j]:
                ans += mat[r][c]
                mat[r][c]=mat[r][j]=-1
                modified = True
print(ans)