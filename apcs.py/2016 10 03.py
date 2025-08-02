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