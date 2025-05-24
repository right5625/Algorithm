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
                parent[i] = n
                deq.append(i)
        cnt += 1
        if cnt == size:
            level += 1
            size = len(deq)
            cnt = 0

N = int(input())
tree = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)
depth = [0] * (N + 1)
vst = [False] * (N + 1)
for _ in range(N - 1):
    v1, v2 = map(int, input().split())
    tree[v1].append(v2)
    tree[v2].append(v1)
BFS(1)
M = int(input())
for _ in range(M):
    v1, v2 = map(int, input().split())
    while depth[v1] != depth[v2]:
        if depth[v1] > depth[v2]:
            v1 = parent[v1]
        else:
            v2 = parent[v2]
    while v1 != v2:
        v1 = parent[v1]
        v2 = parent[v2]
    print(str(v1) + '\n')