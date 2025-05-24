# 조합
import sys
input = lambda : sys.stdin.readline().rstrip()

DP = [[0 for __ in range(30)] for _ in range(30)]
for i in range(30):
    DP[i][1] = i
    DP[i][0] = 1
    DP[i][i] = 1
for i in range(3, 30):
    for j in range(2, i):
        DP[i][j] = DP[i - 1][j] + DP[i - 1][j - 1]
for _ in range(int(input())):
    N, M = map(int, input().split())
    print(DP[M][N])