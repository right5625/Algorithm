from itertools import combinations

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
res = float('inf')
for c in list(combinations(range(N), N // 2)):
    start = c
    link = tuple(set(range(N)) - set(start))
    startAbility = linkAbility = 0
    for i in range(N // 2 - 1):
        for j in range(i + 1, N // 2):
            startAbility += S[start[i]][start[j]] + S[start[j]][start[i]]
    for i in range(N // 2 - 1):
        for j in range(i + 1, N // 2):
            linkAbility += S[link[i]][link[j]] + S[link[j]][link[i]]
    res = min(res, abs(startAbility - linkAbility))
print(res)