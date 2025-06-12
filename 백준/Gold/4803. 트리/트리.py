def dfs(n):
    global cnt1, cnt2
    vst.add(n)
    for i in graph[n]:
        cnt1 += 1
        if i not in vst:
            cnt2 += 1
            dfs(i)

num = 1
while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)
    tree = 0
    vst = set()
    for i in range(1, n + 1):
        if i not in vst:
            cnt1 = cnt2 = 0
            dfs(i)
            if cnt1 == cnt2 * 2:
                tree += 1
    if tree:
        print(f'Case {num}: A forest of {tree} trees.' if tree > 1 else f'Case {num}: There is one tree.')
    else:
        print(f'Case {num}: No trees.')
    num += 1