import sys

R, C, k, m = map(int, input().split())
pop, move = [], [[0]*C for _ in range(R)]

for _ in range(R):
    pop.append(list(map(int, input().split())))

for _ in range(m):
    for i in range(R):
        for j in range(C):
            if pop[i][j] != -1:
                move[i][j] = pop[i][j] // k
    for i in range(R):
        for j in range(C):
            if pop[i][j] != -1:
                if i-1 >= 0:
                    pop[i][j] += move[i-1][j]
                    pop[i-1][j] -= move[i-1][j]
                if i+1 < R:
                    pop[i][j] += move[i+1][j]
                    pop[i+1][j] -= move[i+1][j]
                if j-1 >= 0:
                    pop[i][j] += move[i][j-1]
                    pop[i][j-1] -= move[i][j-1]
                if j+1 < C:
                    pop[i][j] += move[i][j+1]
                    pop[i][j+1] -= move[i][j+1]

maxPop = -sys.maxsize - 1
minPop = sys.maxsize

for i in range(R):
    for j in range(C):
        if pop[i][j] != -1:
            maxPop = max(maxPop, pop[i][j])
            minPop = min(minPop, pop[i][j])

print(minPop)
print(maxPop)