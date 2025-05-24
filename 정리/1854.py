# 다익스트라
import sys, heapq
input = lambda : sys.stdin.readline().rstrip()

n, m, k = map(int, input().split())
A = [[] for _ in range(n + 1)]
D = [[sys.maxsize for __ in range(k)] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    A[a].append((b, c))
D[1][0] = 0
heap = [(0, 1)]
while heap:
    n = heapq.heappop(heap)
    for i in A[n[1]]:
        if D[i[0]][-1] > n[0] + i[1]:
            D[i[0]][-1] = n[0] + i[1]
            D[i[0]].sort()
            heapq.heappush(heap, (n[0] + i[1], i[0]))
for i in D[1:]:
    print(i[k - 1] if i[k - 1] != sys.maxsize else -1)