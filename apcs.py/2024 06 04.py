import bisect

def build_d(arr):
    idx_lst = []
    val_lst = []
    mc = 0
    for i, s in arr:
        mc = max(mc, s)
        idx_lst.append(i)
        val_lst.append(-mc)
    idx_lst.reverse()
    val_lst.reverse()
    return (idx_lst, val_lst)


def solve(a, n, k):
    c = dict()
    t, o, e = 0, 0, 0
    for i in range(n - 1, -1, -1):
        t += a[i]
        if a[i] % 2 == 0:
            e += 1
        else:
            o += 1
        key = o - e
        if key in c:
            c[key].append((i, t))
        else:
            c[key] = [(i, t)]

    d = {}
    for key, arr in c.items():
        d[key] = build_d(arr)

    ans = 0

    psum, key = 0, 0
    for i in range(n):
        psum += a[i]

        if a[i] % 2 == 0:
            key -= 1
        else:
            key += 1

        if key == 0 and psum <= k:
            ans = max(ans, psum)

    psum, key = 0, 0
    for i in range(n - 1, -1, -1):
        psum += a[i]

        if a[i] % 2 == 0:
            key -= 1
        else:
            key += 1

        if key == 0 and psum <= k:
            ans = max(ans, psum)

    psum, key = 0, 0
    for i in range(n):
        psum += a[i]

        if a[i] % 2 == 0:
            key += 1
        else:
            key -= 1

        if key not in d:
            continue

        rr = k - psum
        idx_lst, val_lst = d[key]

        idx_pos = bisect.bisect_right(idx_lst, i)
        val_pos = bisect.bisect_left(val_lst, -rr)

        l = max(idx_pos, val_pos)

        if l < len(val_lst):
            ans = max(ans, psum - val_lst[l])

    return ans


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(a, n, k))

main()