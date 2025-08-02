n = int(input())
lines=[]
for i in range(n):
    pairs = input().split()
    lines.append([int(pairs[0]), int(pairs[1])])
lines.sort(key=lambda x:x[0])
resultLines=[]
curline = lines[0]
for i in range(1, n):
    if(curline[1]<lines[i][0]):
        resultLines.append(curline)
        curline = lines[i]
    elif(curline[1]<lines[i][1]):
        curline = [curline[0], lines[i][1]]
resultLines.append(curline)
length = 0
for rLine in resultLines:
    length = length + (rLine[1]-rLine[0])
print(length)