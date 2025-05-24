# DP
N, L, R = map(int, input().split())
DP = [[[0 for ___ in range(R + 1)] for __ in range(L + 1)] for _ in range(N + 1)]
DP[1][1][1] = 1
for i in range(2, N + 1):
    for j in range(1, L + 1):
        for k in range(1, R + 1):
            DP[i][j][k] = (DP[i - 1][j - 1][k] + DP[i - 1][j][k - 1] + DP[i - 1][j][k] * (i - 2)) % 1000000007
print(DP[N][L][R])