# DP
import sys
input = lambda : sys.stdin.readline().rstrip()

def execute(s, e):
    res = sys.maxsize
    if DP[s][e] != -1:
        return DP[s][e]
    if s == e:
        return 0
    if s + 1 == e:
        return M[s][0] * M[s][1] * M[e][1]
    for i in range(s, e):
        res = min(res, M[s][0] * M[i][1] * M[e][1] + execute(s, i) + execute(i + 1, e))
    DP[s][e] = res
    return DP[s][e]

N = int(input())
M = [(0, 0)]
for _ in range(N):
    x, y = map(int, input().split())
    M.append((x, y))
DP = [[-1 for __ in range(N + 1)] for _ in range(N + 1)]
print(execute(1, N))