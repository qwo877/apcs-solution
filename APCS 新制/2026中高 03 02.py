n, m = map(int, input().split())
queries = list(map(int, input().split()))
performances = [tuple(map(int, input().split())) for _ in range(m)]

# Step 1: 座標壓縮
points = set(queries)
for s, e in performances:
    points.add(s)
    points.add(e + 1)

sorted_pts = sorted(points)
compress = {v: i for i, v in enumerate(sorted_pts)}

# Step 2: 差分陣列
diff = [0] * (len(sorted_pts) + 1)
for s, e in performances:
    diff[compress[s]]     += 1
    diff[compress[e + 1]] -= 1

# Step 3: 前綴和
prefix, running = [], 0
for d in diff[:-1]:
    running += d
    prefix.append(running)

# Step 4: 查詢加總
print(sum(prefix[compress[t]] for t in queries))