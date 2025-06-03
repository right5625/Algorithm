import heapq

n = int(input())
graph = [[] for _ in range(n)]
coordinates = [list(map(float, input().split())) for _ in range(n)]
for i in range(n - 1):
    for j in range(i + 1, n):
        dist = ((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2) ** 0.5
        graph[i].append((dist, j))
        graph[j].append((dist, i))
heap = []
for i in graph[0]:
    heapq.heappush(heap, i)
vst = set()
vst.add(0)
result = 0
while heap:
    d, n = heapq.heappop(heap)
    if n not in vst:
        for i in graph[n]:
            if i[1] not in vst:
                heapq.heappush(heap, i)
        vst.add(n)
        result += d
print(result)