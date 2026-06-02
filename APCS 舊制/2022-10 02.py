def an(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def main():
    n = int(input())  # 接收總共會經過幾個巴士站

    max_ = 0
    min_ = float('inf')

    # 計算相鄰站點之間的最大和最小行進時間
    x_, y_ = map(int, input().split())  # 第一個站點的座標
    for i in range(1, n):
        x_curr, y_curr = map(int, input().split())  # 下一個站點的座標
        d = an(x_, y_, x_curr, y_curr)
        max_ = max(max_, d)
        min_ = min(min_, d)
        x_, y_ = x_curr, y_curr  # 更新前一個站點的座標

    print(max_, min_)

main()
