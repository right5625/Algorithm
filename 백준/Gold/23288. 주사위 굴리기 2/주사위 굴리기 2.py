from collections import deque

N, M, K = map(int, input().split())
A = [[0] * M] + [[0] + list(map(int, input().split())) for _ in range(N)]
S = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
for r in range(1, N + 1):
    for c in range(1, M + 1):
        n = A[r][c]
        q = deque()
        vst = set()
        q.append((r, c))
        vst.add((r, c))
        cnt = 1
        while q:
            cur = q.popleft()
            for i in range(4):
                mr, mc = cur[0] + dr[i], cur[1] + dc[i]
                if 1 <= mr <= N and 1 <= mc <= M and (mr, mc) not in vst and A[mr][mc] == n:
                    q.append((mr, mc))
                    vst.add((mr, mc))
                    cnt += 1
        S[r][c] = n * cnt
curDir = 0
curDice = [6, 3, 5, 4, 2, 1]
curPos = [1, 1]
result = 0
for _ in range(K):
    if curDir == 0 and curPos[1] == M:
        curDir = 2
    elif curDir == 1 and curPos[0] == N:
        curDir = 3
    elif curDir == 2 and curPos[1] == 1:
        curDir = 0
    elif curDir == 3 and curPos[0] == 1:
        curDir = 1
    if curDir == 0:
        curPos[1] += 1
        curDice[0], curDice[1], curDice[3], curDice[5] = curDice[1], curDice[5], curDice[0], curDice[3]
    elif curDir == 1:
        curPos[0] += 1
        curDice[0], curDice[2], curDice[4], curDice[5] = curDice[2], curDice[5], curDice[0], curDice[4]
    elif curDir == 2:
        curPos[1] -= 1
        curDice[0], curDice[1], curDice[3], curDice[5] = curDice[3], curDice[0], curDice[5], curDice[1]
    else:
        curPos[0] -= 1
        curDice[0], curDice[2], curDice[4], curDice[5] = curDice[4], curDice[0], curDice[5], curDice[2]
    result += S[curPos[0]][curPos[1]]
    if curDice[0] > A[curPos[0]][curPos[1]]:
        curDir = (curDir + 1) % 4
    elif curDice[0] < A[curPos[0]][curPos[1]]:
        curDir = curDir - 1 if curDir - 1 >= 0 else 3
print(result)