def main():
    from sys import stdin
    f = [int(x) for x in stdin.readline().split()]
    d = [0] * 40
    d[1] = [f[0], 2+f[0]%2]
    cur, ans = 1, 0
    for x in f[1:]:
        d[cur] [1] -= 1
        if(x > 0):
            ans += abs(d[cur] [0] - x)
            cur += 1
            d[cur] = [x, 2+x%2]
            continue
        while(cur > 0 and d[cur] [1] == 0):
            cur -=1
    print(ans)
main()