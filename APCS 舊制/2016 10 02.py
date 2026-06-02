a, b = map(int, input().split())
s = []
total_sum = 0

# 讀取每一組數字，計算最大值並累加到總和
for i in range(a):
    f = list(map(int, input().split()))
    max_num = max(f)
    total_sum += max_num
    s.append(max_num)

print(total_sum)

# 找到能整除總和的數字並輸出
divisible_nums = []
for num in s:
    if total_sum % num == 0:
        divisible_nums.append(num)

if divisible_nums:
    for i, num in enumerate(divisible_nums):
        if i != 0:
            print(" ", end="")
        print(num, end="")
else:
    print(-1)
