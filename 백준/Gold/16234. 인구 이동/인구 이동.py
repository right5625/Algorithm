import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
res = 0
while True:
    flag = True
    graph = [[[] for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            for i in range(4):
                mr, mc = r + dr[i], c + dc[i]
                if 0 <= mr < N and 0 <= mc < N and L <= abs(A[mr][mc] - A[r][c]) <= R:
                    graph[r][c].append((mr, mc))
                    flag = False
    if flag:
        break
    vst = [[False for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if graph[r][c] and not vst[r][c]:
                q = deque()
                q.append((r, c))
                s = A[r][c]
                vst[r][c] = True
                lst = [(r, c)]
                while q:
                    curR, curC = q.popleft()
                    for nextR, nextC in graph[curR][curC]:
                        if not vst[nextR][nextC]:
                            q.append((nextR, nextC))
                            s += A[nextR][nextC]
                            vst[nextR][nextC] = True
                            lst.append((nextR, nextC))
                size = len(lst)
                for curR, curC in lst:
                    A[curR][curC] = s // size
    res += 1
print(res)