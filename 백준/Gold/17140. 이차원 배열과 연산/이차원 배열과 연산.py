from collections import defaultdict
import copy

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]
rSize = cSize = 3
res = 0
while res < 101:
    if r - 1 < rSize and c - 1 < cSize and A[r - 1][c - 1] == k:
        break
    if rSize >= cSize:
        maxLength = 0
        for i in range(rSize):
            maxLength = max(maxLength, len(set(A[i][j] for j in range(cSize) if A[i][j] != 0)) * 2)
        B = [[0] * maxLength for _ in range(rSize)]
        for i in range(rSize):
            dic = defaultdict(int)
            for j in range(cSize):
                dic[A[i][j]] += 1
            lst = [k for k in sorted(dic.items(), key=lambda x: (x[1], x[0])) if k[0] != 0]
            for j in range(len(lst)):
                if lst[j][0] != 0:
                    B[i][j * 2] = lst[j][0]
                    B[i][j * 2 + 1] = lst[j][1]
        cSize = maxLength
    else:
        maxLength = 0
        for j in range(cSize):
            maxLength = max(maxLength, len(set(A[i][j] for i in range(rSize) if A[i][j] != 0)) * 2)
        B = [[0] * cSize for _ in range(maxLength)]
        for j in range(cSize):
            dic = defaultdict(int)
            for i in range(rSize):
                dic[A[i][j]] += 1
            lst = [k for k in sorted(dic.items(), key=lambda x: (x[1], x[0])) if k[0] != 0]
            for i in range(len(lst)):
                if lst[i][0] != 0:
                    B[i * 2][j] = lst[i][0]
                    B[i * 2 + 1][j] = lst[i][1]
        rSize = maxLength
    A = copy.deepcopy(B)
    res += 1
print(res if res < 101 else -1)