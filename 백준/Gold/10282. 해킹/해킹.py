import sys, heapq
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
    heap = [(0, c)]
    dist = [float('inf')] * (n + 1)
    dist[c] = 0
    vst = set()
    while heap:
        _, node = heapq.heappop(heap)
        if node not in vst:
            vst.add(node)
            for l, d in graph[node]:
                if dist[l] > dist[node] + d:
                    dist[l] = dist[node] + d
                    heapq.heappush(heap, (dist[l], l))
    cnt = time = 0
    for i in dist:
        if i != float('inf'):
            cnt += 1
            time = max(time, i)
    print(cnt, time)