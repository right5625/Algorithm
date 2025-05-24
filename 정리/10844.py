# DP
N = int(input())
DP = [[0 for __ in range(10)] for _ in range(N + 1)]
for i in range(1, 10):
    DP[1][i] = 1
for i in range(2, N + 1):
    DP[i][0] = DP[i - 1][1]
    for j in range(1, 9):
        DP[i][j] = (DP[i - 1][j - 1] + DP[i - 1][j + 1]) % 1000000000
    DP[i][9] = DP[i - 1][8]
print(sum(DP[N][1:]) % 1000000000)