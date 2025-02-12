import sys
from itertools import permutations
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
res = 0
for order in permutations(range(1, 9)):
    seq = list(order[:3]) + [0] + list(order[3:])
    idx = score = 0
    for r in range(N):
        out = 0
        base = [0, 0, 0]
        while out < 3:
            cur = A[r][seq[idx]]
            if cur == 0:
                out += 1
            elif cur == 1:
                score += base[2]
                base = [1, base[0], base[1]]
            elif cur == 2:
                score += base[1] + base[2]
                base = [0, 1, base[0]]
            elif cur == 3:
                score += base[0] + base[1] + base[2]
                base = [0, 0, 1]
            else:
                score += base[0] + base[1] + base[2] + 1
                base = [0, 0, 0]
            idx = idx + 1 if idx + 1 < 9 else 0
    res = max(res, score)
print(res)