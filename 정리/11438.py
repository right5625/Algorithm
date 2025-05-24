# 최소 공통 조상
import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

def BFS(v):
    deq = deque([v])
    vst[v] = True
    level = 1
    size = 1
    cnt = 0
    while deq:
        n = deq.popleft()
        for i in tree[n]:
            if not vst[i]:
                vst[i] = True
                depth[i] = level
                parent[0][i] = n
                deq.append(i)
        cnt += 1
        if cnt == size:
            level += 1
            size = len(deq)
            cnt = 0

N = int(input())
tree = [[] for _ in range(N + 1)]
vst = [False] * (N + 1)
depth = [0] * (N + 1)
size = 1
K = 0
while size <= N:
    size <<= 1
    K += 1
parent = [[0 for __ in range(N + 1)] for _ in range(K + 1)]
for _ in range(N - 1):
    v1, v2 = map(int, input().split())
    tree[v1].append(v2)
    tree[v2].append(v1)
BFS(1)
for k in range(1, K + 1):
    for n in range(1, N + 1):
        parent[k][n] = parent[k - 1][parent[k - 1][n]]
M = int(input())
for _ in range(M):
    v1, v2 = map(int, input().split())
    if depth[v1] > depth[v2]:
        temp = v1
        v1 = v2
        v2 = temp
    for k in range(K, -1, -1):
        if pow(2, k) <= depth[v2] - depth[v1] and depth[v1] <= depth[parent[k][v2]]:
            v2 = parent[k][v2]
    for k in range(K, -1, -1):
        if v1 != v2 and parent[k][v1] != parent[k][v2]:
            v1 = parent[k][v1]
            v2 = parent[k][v2]
    print(str(parent[0][v1] if v1 != v2 else v1) + '\n')