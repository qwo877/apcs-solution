class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 2)
    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i
    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res
    def range_query(self, l, r):
        return self.query(r) - self.query(l - 1)
def dc(arr):
    n = len(arr)
    pos = dict()
    for i, num in enumerate(arr):
        if num not in pos:
            pos[num] = [i + 1]
        else:
            pos[num].append(i + 1)
    bit = BIT(n)
    ans = 0
    for num in sorted(pos.keys()):
        a, b = pos[num]
        if a > b:
            a, b = b, a
        cnt = bit.range_query(a + 1, b - 1)
        ans += cnt
        bit.update(a, 1)
        bit.update(b, 1)
    return ans
n = int(input())
arr = list(map(int, input().split()))
print(dc(arr))