# DP
import sys

lst = list(map(int, input().split()))
move = [[0, 2, 2, 2, 2], [2, 1, 3, 4, 3], [2, 3, 1, 3, 4], [2, 4, 3, 1, 3], [2, 3, 4, 3, 1]]
DP = [[[sys.maxsize for ___ in range(5)] for __ in range(5)] for _ in range(len(lst))]
DP[0][0][0] = 0
cur = 1
for n in lst[:-1]:
    for i in range(5):
        if i != n:
            for j in range(5):
                DP[cur][i][n] = min(DP[cur - 1][i][j] + move[j][n], DP[cur][i][n])
    for i in range(5):
        if i != n:
            for j in range(5):
                DP[cur][n][i] = min(DP[cur - 1][j][i] + move[j][n], DP[cur][n][i])
    cur += 1
print(min(map(min, DP[cur - 1])))