# 위상 정렬
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
m = int(input())
A = [[] for _ in range(n + 1)]
rA = [[] for _ in range(n + 1)]
D = [0] * (n + 1)
for _ in range(m):
    s, e, w = map(int, input().split())
    A[s].append((e, w))
    rA[e].append((s, w))
    D[e] += 1
S, E = map(int, input().split())
deq = deque([S])
res = [0] * (n + 1)
while deq:
    n = deq.popleft()
    for i in A[n]:
        res[i[0]] = max(res[i[0]], res[n] + i[1])
        D[i[0]] -= 1
        if not D[i[0]]:
            deq.append(i[0])
deq.append(E)
cnt = 0
vst = [False] * (n + 1)
vst[E] = True
while deq:
    n = deq.popleft()
    for i in rA[n]:
        if res[n] == res[i[0]] + i[1]:
            cnt += 1
            if not vst[i[0]]:
                vst[i[0]] = True
                deq.append(i[0])
print(res[E])
print(cnt)