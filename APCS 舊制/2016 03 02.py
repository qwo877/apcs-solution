R, C, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(R)]
operations = list(map(int, input().split()))

def reverse_flip(mat):
    return mat[::-1]

def reverse_rotate(mat):
    return [list(row) for row in zip(*mat)][::-1]

for op in reversed(operations):
    if op == 0:
        matrix = reverse_rotate(matrix)
    elif op == 1:
        matrix = reverse_flip(matrix)

R_final = len(matrix)
C_final = len(matrix[0])
print(f"{R_final} {C_final}")
for row in matrix:
    print(' '.join(map(str, row)))