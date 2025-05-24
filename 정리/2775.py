# 조합
import sys
input = lambda : sys.stdin.readline().rstrip()

DP = [[0 for __ in range(15)] for _ in range(15)]
for i in range(1, 15):
    DP[0][i] = i
    DP[i][1] = 1
for i in range(1, 15):
    for j in range(2, 15):
        DP[i][j] = DP[i][j - 1] + DP[i - 1][j]
for _ in range(int(input())):
    k = int(input())
    n = int(input())
    print(DP[k][n])