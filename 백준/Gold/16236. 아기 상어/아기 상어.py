from collections import deque

def findShark():
    for r in range(N):
        for c in range(N):
            if A[r][c] == 9:
                return r, c

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
sharkR, sharkC = findShark()
sharkSize = 2
sharkEat = 0
res = 0
while True:
    minDist = float('inf')
    feedPoint = [float('inf'), float('inf')]

    q = deque()
    q.append((sharkR, sharkC, 0))
    vst = [[False for _ in range(N)] for _ in range(N)]
    vst[sharkR][sharkC] = True
    while q:
        r, c, s = q.popleft()
        if A[r][c] and A[r][c] != 9 and A[r][c] < sharkSize:
            if minDist > s:
                minDist = s
                feedPoint = [r, c]
            elif minDist == s:
                if feedPoint[0] > r:
                    feedPoint = [r, c]
                elif feedPoint[0] == r:
                    feedPoint[1] = min(feedPoint[1], c)
            else:
                break
        for i, j in zip((-1, 1, 0, 0), (0, 0, -1, 1)):
            mr, mc = r + i, c + j
            if 0 <= mr <= N - 1 and 0 <= mc <= N - 1 and A[mr][mc] <= sharkSize and not vst[mr][mc]:
                vst[mr][mc] = True
                q.append((mr, mc, s + 1))
    if minDist == float('inf'):
        break
    A[sharkR][sharkC] = 0
    sharkR, sharkC = feedPoint[0], feedPoint[1]
    A[sharkR][sharkC] = 9
    res += minDist
    sharkEat += 1
    if sharkEat == sharkSize:
        sharkSize += 1
        sharkEat = 0
print(res)