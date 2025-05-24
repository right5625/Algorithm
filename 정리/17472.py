# 최소 신장 트리
import sys, heapq, copy
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

def BFS(i, j):
    deq = deque()
    lst.clear()
    deq.append((i, j))
    lst.append((i, j))
    vst[i][j] = True
    Map[i][j] = num
    while deq:
        r, c = deq.popleft()
        for d in range(4):
            tr = dr[d]
            tc = dc[d]
            while 0 <= r + tr < N and 0 <= c + tc < M:
                if not vst[r + tr][c + tc] and Map[r + tr][c + tc] != 0:
                    Map[r + tr][c + tc] = num
                    vst[r + tr][c + tc] = True
                    deq.append((r + tr, c + tc))
                    lst.append((r + tr, c + tc))
                else:
                    break
                if tr < 0:
                    tr -= 1
                elif tr > 0:
                    tr += 1
                elif tc < 0:
                    tc -= 1
                elif tc > 0:
                    tc += 1
    return lst    

def find(n):
    if n == union[n]:
        return n
    union[n] = find(union[n])
    return union[n]

N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
vst = [[False for __ in range(M)] for _ in range(N)]
num = 1
sum_lst = []
lst = []
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
for i in range(N):
    for j in range(M):
        if Map[i][j] != 0 and not vst[i][j]:
            sum_lst.append(copy.deepcopy(BFS(i, j)))
            num += 1
heap = []
for i in sum_lst:
    for j in i:
        r = j[0]
        c = j[1]
        now = Map[r][c]
        for d in range(4):
            tr = dr[d]
            tc = dc[d]
            length = 0
            while 0 <= r + tr < N and 0 <= c + tc < M:
                if Map[r + tr][c + tc] == now:
                    break
                elif Map[r + tr][c + tc] != 0:
                    if length > 1:
                        heapq.heappush(heap, (length, now, Map[r + tr][c + tc]))
                    break
                else:
                    length += 1
                if tr < 0:
                    tr -= 1
                elif tr > 0:
                    tr += 1
                elif tc < 0:
                    tc -= 1
                elif tc > 0:
                    tc += 1
union = [i for i in range(num)]
edge = 0
res = 0
while heap:
    w, s, e = heapq.heappop(heap)
    s = find(s)
    e = find(e)
    if s != e:
        union[e] = s
        edge += 1
        res += w
print(res if edge == num -2 else -1)