a = 0
b = 0
at = 0
bt = 0
for i in range(4):
    c = sum(map(int, input().split()))
    if i == 0:
        at += c
        a1 = c
    elif i == 1:
        bt += c
        b1 = c
    elif i == 2:
        at += c
        a2 = c
    elif i == 3:
        bt += c
        b2 = c
if a1 > b1:
    a += 1
else:
    b += 1

if a2 > b2:
    a += 1
else:
    b += 1
print(f"{a1}:{b1}")
print(f"{a2}:{b2}")
if a == 2:
    print("Win")
elif b == 2:
    print("Lose")
else:
    print("Tie")
