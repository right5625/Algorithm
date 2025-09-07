N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
result = float('inf')
for i in range(N):
    for j in range(M):
        dis = 0
        for k in range(N):
            for l in range(M):
                dis += (abs(i - k) + abs(j - l)) * A[k][l]
        result = min(result, dis)
print(result)