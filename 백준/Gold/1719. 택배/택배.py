n, m = map(int, input().split())
graph = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s][e] = w
    graph[e][s] = w
result = [[i for i in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    result[i][i] = '-'
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                result[i][j] = result[i][k]
for i in result[1:]:
    print(*i[1:])