import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
cur, div = 1, 2 ** K
for _ in range(N):
    cur = cur * int(input()) % div
print(1 if cur % div == 0 else 0)