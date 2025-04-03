lst = [
    None,
    [[[-1], [1], [0], [0]], [[0], [0], [-1], [1]]],
    [[[0, 0], [-1, 1]], [[-1, 1], [0, 0]]],
    [[[-1, 0], [0, 1], [1, 0], [0, -1]], [[0, 1], [1, 0], [0, -1], [-1, 0]]],
    [[[0, -1, 0], [-1, 0, 1], [0, 1, 0], [1, 0, -1]], [[-1, 0, 1], [0, 1, 0], [1, 0, -1], [0, -1, 0]]],
    [[[-1, 0, 1, 0]], [[0, 1, 0, -1]]]
]

def dfs(idx):
    if idx == cnt:
        blind = 0
        for r in range(N):
            for c in range(M):
                if A[r][c] == 0:
                    blind += 1
        global result
        result = min(result, blind)
        return
    r, c, n = cctv[idx]
    drLst, dcLst = lst[n]
    for dr, dc in zip(drLst, dcLst):
        for i, j in zip(dr, dc):
            mr, mc = r + i, c + j
            while 0 <= mr < N and 0 <= mc < M and A[mr][mc] != 6:
                if A[mr][mc] <= 0:
                    A[mr][mc] -= 1
                mr += i
                mc += j
        dfs(idx + 1)
        for i, j in zip(dr, dc):
            mr, mc = r + i, c + j
            while 0 <= mr < N and 0 <= mc < M and A[mr][mc] != 6:
                if A[mr][mc] <= 0:
                    A[mr][mc] += 1
                mr += i
                mc += j

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
cctv = []
for r in range(N):
    for c in range(M):
        if 1 <= A[r][c] <= 5:
            cctv.append((r, c, A[r][c]))
cnt = len(cctv)
result = N * M
dfs(0)
print(result)