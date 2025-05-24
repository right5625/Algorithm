# DP
import sys
input = lambda : sys.stdin.readline().rstrip()

def tsp(c, v):
    if v == (1 << N) - 1:
        if W[c][0] == 0:
            return float('inf')
        else:
            return W[c][0]
    if DP[c][v] != 0:
        return DP[c][v]
    val = float('inf')
    for i in range(N):
        if (v & (1 << i)) == 0 and W[c][i] != 0:
            val = min(val, tsp(i, v | (1 << i)) + W[c][i])
    DP[c][v] = val
    return DP[c][v]

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
DP = [[0 for __ in range(1 << N)] for _ in range(N)]
print(tsp(0, 1))