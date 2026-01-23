n, a, b = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
result = 0
for i in range(n):
    result = max(result, a / A[i][0], b / A[i][1])
    for j in range(n):
        if i != j:
            result = max(result, a / A[i][0] + b / A[j][1])
print(f'{result:.2f}')