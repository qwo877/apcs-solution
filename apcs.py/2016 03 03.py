'''
1. Sorting Intervals by Start Point

The segments are sorted based on their starting point using seg.sort().

This allows us to process them from left to right in order, which is essential for merging.

2. Greedy Merging of Intervals

The merging process is greedy:

It keeps extending the current interval as long as new segments overlap or are adjacent.

Once it finds a non-overlapping segment, it finalizes the previous one and starts a new merge.

3. Accumulating Total Length

After merging each non-overlapping interval, its length is added to total.

'''

n=int(input())
seg = []
for i in range(n):
    s,t= map(int, input().split())
    seg.append([s,t])
seg.sort()
left, right = 0,0
total = 0
for [s,t] in seg:
    if s <=right:
        right=max(right,t)
    else:
        total +=right-left
        left,right=s,t
total += right -left

print(total)
