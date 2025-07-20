N, M = map(int, input().split())
L = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]
result = 0
for i in range(M - 1):
    result += A[L[i] - 1][L[i + 1] - 1]
print(result)