'''
Problem Simplified:
Given a sequence of numbers, find the first number lower than 60 and the first number higher than 60 (in terms of index: i.e., index of 60 ± 1).
If no number higher than 60 is found, output "worst case".
If no number lower than 60 is found, output "best case".
The first line of output must contain the sorted sequence.
'''

a = int(input())
b = list(map(int, input().split()))
c = sorted(b)
d = next((f for f in c if f >= 60), None)  # Find the first number in list `c` that is greater than or equal to 60. 
                                          # If no such number exists, return `None`.

e = next((f for f in reversed(c) if f < 60), None)  # Find the first number in the reversed list `c` that is less than 60.
                                                    # Effectively, this gets the last number in `c` that is less than 60.
                                                    # If no such number exists, return `None`.
print(*c)#sorted sequence
if e is None:
    print("best case")
else:
    print(e)
if d is None:
    print("worst case")
else:
    print(d)
