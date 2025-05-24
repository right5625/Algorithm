# 트리
import sys
input = lambda : sys.stdin.readline().rstrip()

def DFS(v):
    global cnt
    vst[v] = True
    check = 0
    for i in tree[v]:
        if not vst[i] and i != D:
            check += 1
            DFS(i)
    if not check:
        cnt += 1

N = int(input())
tree = [[] for _ in range(N)]
t = list(map(int, input().split()))
for i in range(N):
    if t[i] != -1:
        tree[t[i]].append(i)
        tree[i].append(t[i])
    else:
        root = i
D = int(input())
cnt = 0
if D != root:
    vst = [False] * N
    DFS(root)
print(cnt)