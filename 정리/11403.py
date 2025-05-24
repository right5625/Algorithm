# 플로이드-워셜
import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            if lst[i][k] and lst[k][j]:
                lst[i][j] = 1
for i in lst:
    print(*i)