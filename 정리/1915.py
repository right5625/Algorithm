# DP
import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
DP = [[0 for __ in range(m)] for _ in range(n)]
for i in range(n):
    N = list(map(int, input()))
    for j in range(m):
        DP[i][j] = N[j]
        if N[j] and i and j:
            DP[i][j] = min(DP[i - 1][j], DP[i][j - 1], DP[i - 1][j - 1]) + 1
print(max(map(max, DP)) ** 2)