# 최소 신장 트리
import sys
input = lambda : sys.stdin.readline().rstrip()

def find(n):
    if n == union[n]:
        return n
    union[n] = find(union[n])
    return union[n]

N = int(input())
edge = []
length = 0
for i in range(N):
    t = input()
    for j in range(N):
        if t[j] != '0':
            if 'a' <= t[j] <= 'z':
                w = ord(t[j]) - ord('a') + 1
            elif 'A' <= t[j] <= 'Z':
                w = ord(t[j]) - ord('A') + 27
            if i != j:
                edge.append((w, i, j))
            length += w
edge.sort()
union = [i for i in range(N)]
cnt = 0
for w, s, e in edge:
    s = find(s)
    e = find(e)
    if s != e:
        union[e] = s
        length -= w
        cnt += 1
        if cnt == N - 1:
            break
print(length if cnt == N - 1 else -1)