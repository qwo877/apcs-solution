F = int(input())
N = int(input())
ys = list(map(int, input().split()))
draw = True
for i in range(N):
    print(F, end=" ")
    if (F == 0 and ys[i] == 2) or (F == 2 and ys[i] == 5) or (F == 5 and ys[i] == 0):
        print(": Won at round {:d}".format(i+1))
        draw = False
        break
    elif (F == 2 and ys[i] == 0) or (F == 5 and ys[i] == 2) or (F == 0 and ys[i] == 5):
        print(": Lost at round {:d}".format(i+1))
        draw = False
        break
    if i >= 1 and ys[i-1] == ys[i]:
        if ys[i] == 0: F = 5
        elif ys[i] == 2: F = 0
        elif ys[i] == 5: F = 2
    else:
        if ys[i] == 0: F = 0
        elif ys[i] == 2: F = 2
        elif ys[i] == 5: F = 5
if draw: print(": Drew at round {:d}".format(N))
