# 조합
N, K = map(int, input().split())
DP = [[0 for __ in range(N + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    DP[i][1] = i
    DP[i][0] = 1
    DP[i][i] = 1
for i in range(3, N + 1):
    for j in range(2, i):
        DP[i][j] =(DP[i - 1][j - 1] + DP[i - 1][j]) % 10007
print(DP[N][K])