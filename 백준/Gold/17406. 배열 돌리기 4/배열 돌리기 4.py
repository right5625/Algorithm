from itertools import permutations
import copy

N, M, K = map(int, input().split())
A = [[0] * (M + 1)]
for _ in range(N):
    A.append([0] + list(map(int, input().split())))
rcs = [list(map(int, input().split())) for _ in range(K)]
seqLst = list(permutations(range(K)))
res = float('inf')
for seq in seqLst:
    B = copy.deepcopy(A)
    for n in seq:
        r, c, s = rcs[n][0], rcs[n][1], rcs[n][2]
        minR, minC, maxR, maxC = r - s, c - s, r + s, c + s
        while minR != maxR:
            t = B[minR][minC]
            for i in range(minR + 1, maxR + 1):
                B[i - 1][minC] = B[i][minC]
            for i in range(minC + 1, maxC + 1):
                B[maxR][i - 1] = B[maxR][i]
            for i in range(maxR - 1, minR - 1, -1):
                B[i + 1][maxC] = B[i][maxC]
            for i in range(maxC - 1, minC - 1, -1):
                B[minR][i + 1] = B[minR][i]
            B[minR][minC + 1] = t
            minR += 1
            minC += 1
            maxR -= 1
            maxC -= 1
    for i in B[1:]:
        res = min(res, sum(i[1:]))
print(res)