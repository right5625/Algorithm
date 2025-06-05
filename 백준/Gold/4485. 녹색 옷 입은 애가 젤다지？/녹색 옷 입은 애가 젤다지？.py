import heapq

dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
num = 1
while True:
    N = int(input())
    if N == 0:
        break
    A = [list(map(int, input().split())) for _ in range(N)]
    dist = [[float('inf') for _ in range(N)] for _ in range(N)]
    dist[0][0] = A[0][0]
    vst = set()
    vst.add((0, 0))
    heap = [(dist[0][0], (0, 0))]
    while heap:
        d, rc = heapq.heappop(heap)
        for i in range(4):
            mr, mc = rc[0] + dr[i], rc[1] + dc[i]
            if 0 <= mr < N and 0 <= mc < N and (mr, mc) not in vst:
                if dist[mr][mc] > d + A[mr][mc]:
                    dist[mr][mc] = d + A[mr][mc]
                    heapq.heappush(heap, (dist[mr][mc], (mr, mc)))
                vst.add((mr, mc))
    print(f'Problem {num}: {dist[N - 1][N - 1]}')
    num += 1