# 플로이드-워셜
import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
D = [[sys.maxsize for __ in range(N + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    D[i][i] = 0
for _ in range(M):
    s, e = map(int, input().split())
    D[s][e] = 1
    D[e][s] = 1
for k in range(1, N + 1):
    for s in range(1, N + 1):
        for e in range(1, N + 1):
            D[s][e] = min(D[s][e], D[s][k] + D[k][e])
res = [sum(i[1:]) for i in D[1:]]
print(res.index(min(res)) + 1)