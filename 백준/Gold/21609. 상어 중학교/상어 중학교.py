import copy
from collections import deque

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
res = 0
while True:
    maxCnt = 1
    rainbowMaxCnt = 0
    maxRC = [-1, -1]
    maxGroup = []
    B = copy.deepcopy(A)
    for r in range(N):
        for c in range(N):
            if B[r][c] > 0:
                q = deque()
                q.append((r, c))
                vst = [[False for _ in range(N)] for _ in range(N)]
                vst[r][c] = True
                cnt = 0
                rainbowCnt = 0
                group = []
                while q:
                    curR, curC = q.popleft()
                    cnt += 1
                    if B[curR][curC] == 0:
                        rainbowCnt += 1
                    group.append((curR, curC))
                    for i in range(4):
                        mr, mc = curR + dr[i], curC + dc[i]
                        if 0 <= mr < N and 0 <= mc < N and not vst[mr][mc] and B[mr][mc] in [B[r][c], 0]:
                            vst[mr][mc] = True
                            q.append((mr, mc))
                            if B[r][c] == B[mr][mc]:
                                B[mr][mc] = -2
                B[r][c] = -2
                if maxCnt < cnt:
                    maxCnt = cnt
                    rainbowMaxCnt = rainbowCnt
                    maxRC = [r, c]
                    maxGroup = group
                elif maxCnt == cnt:
                    if rainbowMaxCnt < rainbowCnt:
                        rainbowMaxCnt = rainbowCnt
                        maxRC = [r, c]
                        maxGroup = group
                    elif rainbowMaxCnt == rainbowCnt:
                        if maxRC[0] < r:
                            maxRC = [r, c]
                            maxGroup = group
                        elif maxRC[0] == r:
                            maxRC[1] = max(maxRC[1], c)
                            maxGroup = group
    if maxCnt == 1:
        break
    for r, c in maxGroup:
        A[r][c] = -2
    res += maxCnt * maxCnt
    for r in range(N - 2, -1, -1):
        for c in range(N):
            if A[r][c] >= 0:
                for i in range(r, N - 1):
                    if A[i + 1][c] == -1:
                        break
                    elif A[i + 1][c] == -2:
                        A[i][c], A[i + 1][c] = A[i + 1][c], A[i][c]
    B = copy.deepcopy(A)
    for r in range(N):
        for c in range(N):
            B[r][c] = A[c][N - 1 - r]
    A = B
    for r in range(N - 2, -1, -1):
        for c in range(N):
            if A[r][c] >= 0:
                for i in range(r, N - 1):
                    if A[i + 1][c] == -1:
                        break
                    elif A[i + 1][c] == -2:
                        A[i][c], A[i + 1][c] = A[i + 1][c], A[i][c]
print(res)