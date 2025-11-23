import sys
input = lambda: sys.stdin.readline().rstrip()

def find(v):
    if parent[v] == v:
        return v
    parent[v] = find(parent[v])
    return parent[v]

def union(v1, v2):
    a = find(v1)
    b = find(v2)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M, K = map(int, input().split())
edges = [(0, 0)]
for i in range(1, M + 1):
    x, y = map(int, input().split())
    edges.append((x, y))
impossible_edges = [False] * (M + 1)
result = [0] * K
for i in range(K):
    parent = [j for j in range(N + 1)]
    min_weight = use = score = 0
    for weight in range(1, M + 1):
        if impossible_edges[weight]:
            continue
        vertex1, vertex2 = edges[weight]
        if find(vertex1) != find(vertex2):
            union(vertex1, vertex2)
            score += weight
            use += 1
            if min_weight == 0:
                min_weight = weight
    if use < N - 1:
        break
    impossible_edges[min_weight] = True
    result[i] = score
print(*result)