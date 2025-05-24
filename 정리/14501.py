# DP
import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
T = [0] * (N + 1)
P = [0] * (N + 1)
for i in range(1, N + 1):
    T[i], P[i] = map(int, input().split())
DP = [0] * (N + 2)
for i in range(N, 0, -1):
    if i + T[i] > N + 1:
        DP[i] = DP[i + 1]
    else:
        DP[i] = max(DP[i + 1], DP[i + T[i]] + P[i])
print(DP[1])