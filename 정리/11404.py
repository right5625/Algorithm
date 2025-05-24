# 플로이드-워셜
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
D = [[sys.maxsize for __ in range(n + 1)] for _ in range(n + 1)]
for i in range(n + 1):
    D[i][i] = 0
m = int(input())
for _ in range(m):
    s, e, w = map(int, input().split())
    D[s][e] = min(D[s][e], w)
for k in range(1, n + 1):
    for s in range(1, n + 1):
        for e in range(1, n + 1):
            D[s][e] = min(D[s][e], D[s][k] + D[k][e])
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if D[i][j] == sys.maxsize:
            print(0, end = ' ')
        else:
            print(D[i][j], end = ' ')
    print()