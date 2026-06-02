a1, a2, a3 = map(int, input().split())
count_dict = {}
for num in [a1, a2, a3]:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1
max_count = max(count_dict.values())
most_common_numbers = [key for key, value in count_dict.items() if value == max_count]
print(max_count, end=' ')
unique_numbers = sorted(set([a1, a2, a3]), reverse=True)
for num in unique_numbers:
    print(num, end=' ')
