from itertools import combinations

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
home = []
chicken = []
for r in range(N):
    for c in range(N):
        if A[r][c] == 1:
            home.append((r, c))
        elif A[r][c] == 2:
            chicken.append((r, c))
length = len(home)
res = float('inf')
for i in list(combinations(range(len(chicken)), M)):
    chickenDist = [float('inf')] * length
    for j in range(length):
        for k in i:
            chickenDist[j] = min(chickenDist[j], abs(home[j][0] - chicken[k][0]) + abs(home[j][1] - chicken[k][1]))
    res = min(res, sum(chickenDist))
print(res)