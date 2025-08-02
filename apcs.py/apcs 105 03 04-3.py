A=0
B=0
a=input().strip()
for i in range(len(a)):
    if i%2==0:
        A=A+int(a[i])
    else:
        B=B+int(a[i])
c=abs(A-B)
print(c)