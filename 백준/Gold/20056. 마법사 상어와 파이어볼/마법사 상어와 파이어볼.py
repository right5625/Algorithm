from collections import deque
import copy

N, M, K = map(int, input().split())
A = [[deque() for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    A[r - 1][c - 1].append((m, s, d))
dr, dc = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
for _ in range(K):
    B = [[deque() for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            while A[r][c]:
                m, s, d = A[r][c].popleft()
                curR, curC = r, c
                for j in range(s):
                    curR += dr[d]
                    curC += dc[d]
                    if curR == -1:
                        curR = N - 1
                    elif curR == N:
                        curR = 0
                    if curC == -1:
                        curC = N - 1
                    elif curC == N:
                        curC = 0
                B[curR][curC].append((m, s, d))
    for r in range(N):
        for c in range(N):
            cnt = len(B[r][c])
            if cnt > 1:
                m, s, d = 0, 0, []
                while B[r][c]:
                    mi, si, di = B[r][c].popleft()
                    m += mi
                    s += si
                    d.append(di)
                m, s = m // 5, s // cnt
                if m > 0:
                    for i in ([0, 2, 4, 6] if len(list(filter(lambda x: x % 2 == 0, d))) in [0, cnt] else [1, 3, 5, 7]):
                        B[r][c].append((m, s, i))
    A = copy.deepcopy(B)
result = 0
for r in range(N):
    for c in range(N):
        while A[r][c]:
            result += A[r][c].popleft()[0]
print(result)