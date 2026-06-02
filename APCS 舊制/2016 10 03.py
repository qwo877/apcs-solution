def lucky_person(N, M, K):
    people = list(range(1, N + 1))
    pos = 0
    for _ in range(K):
        pos = (pos + M - 1) % len(people)
        people.pop(pos)
        if pos == len(people):
            pos = 0
    return people[pos]

N, M, K = map(int, input().split())
print(lucky_person(N, M, K))

'''
N,M,K=map(int, input().split())
a = list(range(1, N + 1))
k1 = 0
for _ in range(K):
    k1 = (k1 + M - 1) % len(a)
    e= a.pop(k1)
o = a[k1 % len(a)]
print(o)
'''