n = int(input())
p=[]
for i in range(n):
    p.append([int(x) for x in input().split()])
    p.sort(key=lambda y:y[0]**2 + y[1]**2)
print(p[-2][0],p[-2][1])