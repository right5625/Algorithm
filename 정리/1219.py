# 벨만-포드
import sys
input = lambda : sys.stdin.readline().rstrip()

N, start, end, M = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(M)]
P = list(map(int, input().split()))
D = [-sys.maxsize] * N
D[start] = P[start]
for i in range(N * 2):
    for s, e, w in E:
        if D[s] == sys.maxsize:
            D[e] = sys.maxsize
        elif D[s] != -sys.maxsize and D[e] < D[s] + (P[e] - w):
            D[e] = sys.maxsize if i > N - 1 else D[s] + (P[e] - w)
if D[end] == -sys.maxsize:
    print('gg')
elif D[end] == sys.maxsize:
    print('Gee')
else:
    print(D[end])