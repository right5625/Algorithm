from itertools import combinations
from collections import deque

def bfs(com):
    q = deque()
    vst = [False] * (N + 1)
    q.append(com[0])
    vst[com[0]] = True
    cnt = 1
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if not vst[i] and i in com:
                q.append(i)
                vst[i] = True
                cnt += 1
    return cnt

N = int(input())
A = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in list(map(int, input().split()))[1:]:
        graph[i].append(j)
vst = [False] * (N + 1)
lst = []
for i in range(1, N + 1):
    if not vst[i]:
        q = deque()
        q.append(i)
        vst[i] = True
        s = 0
        while q:
            cur = q.popleft()
            s += A[cur]
            for j in graph[cur]:
                if not vst[j]:
                    q.append(j)
                    vst[j] = True
        lst.append(s)
res = float('inf')
if len(lst) == 1:
    arr = set(range(1, N + 1))
    for i in range(1, N // 2 + 1):
        for com1 in combinations(arr, i):
            com2 = tuple(arr - set(com1))
            if bfs(com1) + bfs(com2) == N:
                res = min(res, abs(sum(A[j] for j in com1) - sum(A[j] for j in com2)))
elif len(lst) == 2:
    res = abs(lst[0] - lst[1])
print(res if res != float('inf') else -1)