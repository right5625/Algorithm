from itertools import combinations
import copy

def dfs(r, c):
    for i in range(4):
        mr, mc = r + dr[i], c + dc[i]
        if 0 <= mr < N and 0 <= mc < M and B[mr][mc] == 0:
            B[mr][mc] = 2
            dfs(mr, mc)

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
blank = [(r, c) for r in range(N) for c in range(M) if A[r][c] == 0]
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
res = 0
for i in list(combinations(blank, 3)):
    B = copy.deepcopy(A)
    B[i[0][0]][i[0][1]] = B[i[1][0]][i[1][1]] = B[i[2][0]][i[2][1]] = 1
    for r in range(N):
        for c in range(M):
            if B[r][c] == 2:
                dfs(r, c)
    cnt = 0
    for r in range(N):
        for c in range(M):
            if B[r][c] == 0:
                cnt += 1
    res = max(res, cnt)
print(res)