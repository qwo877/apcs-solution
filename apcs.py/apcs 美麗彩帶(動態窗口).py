M, N = map(int, input().split())
A = [x for x in input().split()]
cnt = {} # number of occurrence
answer = 0
for i in range(N):
    # Add A[i]
    if A[i] in cnt:
        cnt[A[i]] += 1
    else:
        cnt[A[i]] = 1
    # Remove A[i - M]
    if i >= M:
        cnt[A[i - M]] -= 1
        if cnt[A[i - M]] == 0:
            cnt.pop(A[i - M])
    if i >= M - 1:
        if len(cnt) == M:
            answer += 1
print(answer)