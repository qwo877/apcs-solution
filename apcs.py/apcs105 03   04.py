a = int(input())
b = list(map(int, input().split()))
c = sorted(b)
d = next((f for f in c if f >= 60), None)
e = next((f for f in reversed(c) if f < 60), None)
print(*c)
if e is None:
    print("best case")
else:
    print(e)
if d is None:
    print("worst case")
else:
    print(d)
