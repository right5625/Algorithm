import heapq

def find(v):
    if parent[v] == v:
        return v
    parent[v] = find(parent[v])
    return parent[v]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
coordinates = [[]] + [list(map(int, input().split())) for _ in range(N)]
heap = []
for i in range(1, N):
    for j in range(i + 1, N + 1):
        heapq.heappush(heap, ((((coordinates[i][0] - coordinates[j][0]) ** 2) + ((coordinates[i][1] - coordinates[j][1]) ** 2)) ** 0.5, i, j))
parent = [i for i in range(N + 1)]
use = 0
for _ in range(M):
    s, e = map(int, input().split())
    if find(s) != find(e):
        union(s, e)
        use += 1
result = 0
while use < N - 1:
    d, s, e = heapq.heappop(heap)
    if find(s) != find(e):
        union(s, e)
        result += d
        use += 1
print(f'{result:.2f}')