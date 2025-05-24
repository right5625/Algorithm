# 다익스트라
import sys, heapq
input = lambda : sys.stdin.readline().rstrip()

V, E = map(int, input().split())
K = int(input())
A = [[] for _ in range(V + 1)]
D = [sys.maxsize] * (V + 1)
vst = [False] * (V + 1)
D[K] = 0
for _ in range(E):
    u, v, w = map(int, input().split())
    A[u].append((v, w))
heap = [(0, K)]
while heap:
    n = heapq.heappop(heap)
    if not vst[n[1]]:
        vst[n[1]] = True
        for i in A[n[1]]:
            if D[i[0]] > D[n[1]] + i[1]:
                D[i[0]] = D[n[1]] + i[1]
                heapq.heappush(heap, (D[i[0]], i[0]))
for i in range(1, V + 1):
    print(D[i] if vst[i] else 'INF')