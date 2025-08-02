import itertools

def a(c, s, k):
    b = set(''.join(p) for p in itertools.product(c, repeat=k))
    for i in range(len(s) - k + 1):
        sub = s[i:i+k]
        if sub in b:
            b.remove(sub)

    return min(b) if b else None

c = list(input())
k=int(input())
s = input()
print(a(c, s, k))