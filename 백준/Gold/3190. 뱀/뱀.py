from collections import deque

N = int(input())
A = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(int(input())):
    r, c = map(int, input().split())
    A[r - 1][c - 1] = 1
dic = {}
for _ in range(int(input())):
    X, C = input().split()
    dic[int(X)] = C
cur = (0, 0, 0)
dr, dc = (0, 1, 0, -1), (1, 0, -1, 0)
q = deque()
q.append((0, 0))
sec = 0
while True:
    r, c, d = cur
    mr, mc = r + dr[d], c + dc[d]
    sec += 1
    if mr < 0 or mr >= N or mc < 0 or mc >= N or (mr, mc) in q:
        break
    q.append((mr, mc))
    if A[mr][mc] == 1:
        A[mr][mc] = 0
    else:
        q.popleft()
    if sec in dic.keys():
        d = (d + 3) % 4 if dic[sec] == 'L' else (d + 1) % 4
    cur = (mr, mc, d)
print(sec)