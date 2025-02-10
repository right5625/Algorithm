from collections import deque

def solution(n, wires):
    result = float('inf')
    for i in range(n - 1):
        graph = [[] for _ in range(n + 1)]
        for j in range(n - 1):
            if i == j:
                continue
            graph[wires[j][0]].append(wires[j][1])
            graph[wires[j][1]].append(wires[j][0])
        vst = [False] * (n + 1)
        lst = []
        for j in range(1, n + 1):
            if not vst[j]:
                q = deque()
                q.append(j)
                vst[j] = True
                cnt = 1
                while q:
                    cur = q.popleft()
                    for k in graph[cur]:
                        if not vst[k]:
                            q.append(k)
                            vst[k] = True
                            cnt += 1
                lst.append(cnt)
        result = min(result, abs(lst[0] - lst[1]))
    return result