import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
D = {i[0]: i[1:] for i in [list(map(int, input().split())) for _ in range(N * N)]}
A = [[0 for _ in range(N)] for _ in range(N)]
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
for k, v in D.items():
    pos1 = []
    maxCnt = 0
    for r in range(N):
        for c in range(N):
            if A[r][c] == 0:
                cnt = 0
                for j in range(4):
                    mr, mc = r + dr[j], c + dc[j]
                    if 0 <= mr <= N - 1 and 0 <= mc <= N - 1 and A[mr][mc] in v:
                        cnt += 1
                if maxCnt < cnt:
                    maxCnt = cnt
                    pos1 = [[r, c]]
                elif maxCnt == cnt:
                    pos1.append([r, c])
    if len(pos1) == 1:
        A[pos1[0][0]][pos1[0][1]] = k
        continue
    pos2 = []
    maxCnt = 0
    for r, c in pos1:
        cnt = 0
        for j in range(4):
            mr, mc = r + dr[j], c + dc[j]
            if 0 <= mr <= N - 1 and 0 <= mc <= N - 1 and A[mr][mc] == 0:
                cnt += 1
        if maxCnt < cnt:
            maxCnt = cnt
            pos2 = [[r, c]]
        elif maxCnt == cnt:
            pos2.append([r, c])
    if len(pos2) == 1:
        A[pos2[0][0]][pos2[0][1]] = k
        continue
    pos3 = [float('inf'), float('inf')]
    for r, c in pos2:
        if r < pos3[0]:
            pos3 = [r, c]
        elif r == pos3[0]:
            pos3[1] = min(pos3[1], c)
    A[pos3[0]][pos3[1]] = k
S = [0, 1, 10, 100, 1000]
res = 0
for r in range(N):
    for c in range(N):
        cnt = 0
        for i in range(4):
            mr, mc = r + dr[i], c + dc[i]
            if 0 <= mr <= N - 1 and 0 <= mc <= N - 1 and A[mr][mc] in D[A[r][c]]:
                cnt += 1
        res += S[cnt]
print(res)