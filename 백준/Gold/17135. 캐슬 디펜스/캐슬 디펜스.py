import copy

def attack(i, j, k):
    global cnt
    s = set()
    for p in [i, j, k]:
        maxDist = float('inf')
        rc = (float('inf'), float('inf'))
        for r in range(N):
            for c in range(M):
                dist = abs(r - N) + abs(c - p)
                if C[r][c] and dist <= D:
                    if maxDist > dist:
                        maxDist = dist
                        rc = (r, c)
                    elif maxDist == dist:
                        if rc[1] > c:
                            rc = (r, c)
        if rc[0] != float('inf'):
            s.add(rc)
    for r, c in s:
        C[r][c] = 0
    cnt += len(s)

def lotation():
    for r in range(N - 2, -1, -1):
        for c in range(M):
            C[r + 1][c] = C[r][c]
    for c in range(M):
        C[0][c] = 0

N, M, D = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
res = 0
for i in range(M - 2):
    for j in range(i + 1, M - 1):
        for k in range(j + 1, M):
            C = copy.deepcopy(A)
            cnt = 0
            for _ in range(N):
                attack(i, j, k)
                lotation()
            res = max(res, cnt)
print(res)