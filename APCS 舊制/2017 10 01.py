a, b, r = map(bool, [int(x) for x in input().split()])
AND = a & b == r
OR = a | b == r
XOR = a ^ b == r
if AND:
    print("AND")
if OR:
    print("OR")
if XOR:
    print("XOR")
if not (AND or OR or XOR):
    print("IMPOSSIBLE")