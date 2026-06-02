def rl(bit_string):
    result = []
    count = 1
    current = bit_string[0]
    for i in range(1, len(bit_string)):
        if bit_string[i] == current:
            count += 1
            if count > 7:  # 超過7就要分段
                result.append(f"{current}111")  # 最大只能表示7，所以是'111'
                count = 1  # 重新開始新的段
        else:
            result.append(f"{current}{format(count, '03b')}")  # 轉成3位二進位表示法
            current = bit_string[i]
            count = 1
    # 最後一段
    result.append(f"{current}{format(count, '03b')}")
    return result

def p(original_len, compressed_len):
    return round((compressed_len / original_len) * 100)

def f(test_case):
    # 檢查是否只包含 '0' 和 '1'
    if not all(c in {'0', '1'} for c in test_case):
        return "-1"
    # 執行跑長編碼
    compressed = rl(test_case)
    # 原始位元個數
    original_len = len(test_case)
    # 壓縮後的位元個數
    compressed_len = len(compressed) * 4  # 每個碼字是4位元
    # 計算壓縮率
    compression_rate = p(original_len, compressed_len)
    # 回傳結果：壓縮碼字 + 壓縮率
    return " ".join(compressed) + f" {compression_rate}%"
# 主程式
n = int(input())
for _ in range(n):
    test_case = input().strip()
    print(f(test_case))