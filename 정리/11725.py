# 트리
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

def BFS():
    deq = deque([1])
    vst[1] = True
    while deq:
        n = deq.popleft()
        for i in A[n]:
            if not vst[i]:
                vst[i] = True
                deq.append(i)
                res[i] = n
    
N = int(input())
A = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)
vst = [False] * (N + 1) 
res = [0] * (N + 1)
BFS()
print(*res[2:], sep = '\n')