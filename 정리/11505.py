# 세그먼트 트리
import sys
input = lambda : sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())
mod = 1000000007
size = 2
while size < N:
    size *= 2
tree = [1] * (size * 2)
for i in range(N):
    tree[size + i] = int(input())
for i in range(size - 1, 0, -1):
    tree[i] = tree[i * 2] * tree[i * 2 + 1] % mod
for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        tree[size + b - 1] = c
        idx = (size + b - 1) // 2
        while idx > 0:
            tree[idx] = tree[idx * 2] * tree[idx * 2 + 1] % mod
            idx //= 2
    else:
        start = size + b - 1
        end = size + c - 1
        res = 1
        while start <= end:
            if start % 2 == 1:
                res = res * tree[start] % mod
            if end % 2 == 0:
                res = res * tree[end] % mod
            start = (start + 1) // 2
            end = (end - 1) // 2
        print(res)