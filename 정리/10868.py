# 세그먼트 트리
import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
size = 2
while size < N:
    size *= 2
tree = [0] * (size * 2)
for i in range(N):
    tree[size + i] = int(input())
for i in range(size - 1, 0, -1):
    tree[i] = min(tree[i * 2], tree[i * 2 + 1])
for _ in range(M):
    a, b = map(int, input().split())
    start = size + a - 1
    end = size + b - 1
    res = sys.maxsize
    while start <= end:
        if start % 2 == 1:
            res = min(res, tree[start])
        if end % 2 == 0:
            res = min(res, tree[end])
        start = (start + 1) // 2
        end = (end - 1) // 2
    print(res)