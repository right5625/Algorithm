# 다익스트라
import sys, heapq
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
M = int(input())
A = [[] for _ in range(N + 1)]
D = [sys.maxsize] * (N + 1)
vst = [False] * (N + 1)
for _ in range(M):
    s, e, w = map(int, input().split())
    A[s].append((e, w))
start, end = map(int, input().split())
D[start] = 0
heap = [(0, start)]
while heap:
    n = heapq.heappop(heap)
    if not vst[n[1]]:
        vst[n[1]] = True
        for i in A[n[1]]:
            if D[i[0]] > D[n[1]] + i[1]:
                D[i[0]] = D[n[1]] + i[1]
                heapq.heappush(heap, (D[i[0]], i[0]))
print(D[end])