from collections import deque

N, M = map(int, input().split())
G1 = [[] for _ in range(N + 1)]
G2 = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    G1[a].append(b)
    G2[b].append(a)
res = 0
for i in range(1, N + 1):
    q = deque([i])
    vst = [False] * (N + 1)
    vst[i] = True
    cnt1 = 0
    while q:
        cur = q.popleft()
        for j in G1[cur]:
            if not vst[j]:
                q.append(j)
                vst[j] = True
                cnt1 += 1
    q = deque([i])
    vst = [False] * (N + 1)
    vst[i] = True
    cnt2 = 0
    while q:
        cur = q.popleft()
        for j in G2[cur]:
            if not vst[j]:
                q.append(j)
                vst[j] = True
                cnt2 += 1
    if cnt1 + cnt2 == N - 1:
        res += 1
print(res)