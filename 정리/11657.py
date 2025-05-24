# 벨만-포드
import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(M)]
D = [sys.maxsize] * (N + 1)
D[1] = 0
for i in range(N - 1):
    for s, e, w in E:
        if D[s] != sys.maxsize and D[e] > D[s] + w:
            D[e] = D[s] + w
flag = False
for s, e, w in E:
    if D[s] != sys.maxsize and D[e] > D[s] + w:
        flag = True
        break
if flag:
    print(-1)
else:
    for i in D[2:]:
        print(i if i != sys.maxsize else -1)