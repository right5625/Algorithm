import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
dic = {(r, c): False for r in range(N) for c in range(N)}
dic[(N - 2, 0)] = dic[(N - 2, 1)] = dic[(N - 1, 0)] = dic[(N - 1, 1)] = True
dr, dc = (0, 0, -1, -1, -1, 0, 1, 1, 1), (0, -1, -1, 0, 1, 1, 1, 0, -1)
diagR, diagC = (-1, -1, 1, 1), (-1, 1, -1, 1)
for _ in range(M):
    d, s = map(int, input().split())
    B = []
    for r in range(N):
        for c in range(N):
            if dic[(r, c)]:
                mr, mc = (r + dr[d] * s) % N, (c + dc[d] * s) % N
                A[mr][mc] += 1
                B.append((mr, mc))
                dic[(r, c)] = False
    for r, c in B:
        dic[(r, c)] = True
    for r in range(N):
        for c in range(N):
            if dic[(r, c)]:
                cnt = 0
                for i in range(4):
                    mr, mc = r + diagR[i], c + diagC[i]
                    if 0 <= mr < N and 0 <= mc < N and A[mr][mc]:
                        cnt += 1
                A[r][c] += cnt
    for r in range(N):
        for c in range(N):
            if dic[(r, c)]:
                dic[(r, c)] = False
            elif A[r][c] >= 2 and not dic[(r, c)]:
                A[r][c] -= 2
                dic[(r, c)] = True
print(sum(A[r][c] for r in range(N) for c in range(N)))