k, q, r = [int(x) for x in input().split()]
s = list(input())

ops = []
for _ in range(q):
    nums = [int(x) for x in input().split()]
    newS = ['']*k

    for i in range(len(nums)):
        newS[nums[i]-1]=s[i]

    s = newS
    ops.append(s)

ss = list(zip(*ops))
for i in range(r):
    print(''.join(ss[i]))