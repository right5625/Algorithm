# 최소 신장 트리
import sys
input = lambda : sys.stdin.readline().rstrip()

def find(n):
    if n == union[n]:
        return n
    union[n] = find(union[n])
    return union[n]

V, E = map(int, input().split())
edge = []
union = [i for i in range(V + 1)]
for _ in range(E):
    s, e, w = map(int, input().split())
    edge.append((w, s, e))
edge.sort()
weight = []
for w, s, e in edge:
    s = find(s)
    e = find(e)
    if s != e:
        weight.append(w)
        union[e] = s
        if len(weight) == V - 1:
            break
print(sum(weight))