# 조합
N, M, K = map(int, input().split())
DP = [[0 for __ in range(N + M + 1)] for _ in range(N + M + 1)]
for i in range(N + M + 1):
    for j in range(i + 1):
        if j == 0 or j == i:
            DP[i][j] = 1
        else:
            DP[i][j] = DP[i - 1][j - 1] + DP[i - 1][j]
if DP[N + M][M] < K:
    print(-1)
else:
    res = ''
    while not (N == 0 and M == 0):
        T = DP[N - 1 + M][M]
        if T >= K:
            res += 'a'
            N -= 1
        else:
            res += 'z'
            K -= T
            M -= 1
    print(res)