# 기하(CCW)
import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
pos = [tuple(map(int, input().split())) for _ in range(N)]
res = pos[N - 1][0] * pos[0][1] - pos[N - 1][1] * pos[0][0]
for i in range(N - 1):
    res += pos[i][0] * pos[i + 1][1] - pos[i][1] * pos[i + 1][0]
print(f'{round(abs(res / 2), 1):.1f}')