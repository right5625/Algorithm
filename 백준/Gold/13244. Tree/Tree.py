def dfs(n):
    global cnt
    vst.add(n)
    for i in graph[n]:
        if i not in vst:
            cnt += 1
            dfs(i)

for _ in range(int(input())):
    N = int(input())
    graph = [[] for _ in range(N + 1)]
    M = int(input())
    for _ in range(M):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)
    vst = set()
    cnt = 0
    dfs(1)
    print('tree' if len(vst) == N and cnt == M else 'graph')