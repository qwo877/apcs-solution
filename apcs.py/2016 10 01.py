a=list(map(int,input().split()))
print(*sorted(a))
a,b,c=sorted(a)
if a + b <= c:
        print("No")
elif a * a + b * b < c * c:
    print("Obtuse")
elif a * a + b * b == c * c:
    print("Right")
else:
    print("Acute")