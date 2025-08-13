N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
result = [float('inf')]
for i in range(N):
    for j in range(M):
        d = (i + 1) + abs((M + 1) // 2 - (j + 1))
        if not A[i][j] and result[0] > d:
            result = [d, (i + 1), (j + 1)]
print(-1 if result[0] == float('inf') else f'{result[1]} {result[2]}')