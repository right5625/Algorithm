late = (0.05, 0.01, 0.07, 0.1, 0.02, 0.01, 0.07, 0.1, 0.02)
dr = ((0, -1, -1, -1, -2, 1, 1, 1, 2), (3, 0, 1, 2, 1, 0, 1, 2, 1), (0, -1, -1, -1, -2, 1, 1, 1, 2), (-3, 0, -1, -2, -1, 0, -1, -2, -1))
dc = ((-3, 0, -1, -2, -1, 0, -1, -2, -1), (0, -1, -1, -1, -2, 1, 1, 1, 2), (3, 0, 1, 2, 1, 0, 1, 2, 1), (0, -1, -1, -1, -2, 1, 1, 1, 2))

def tornado(r, c, ar, ac):
    global result
    n = A[r][c]
    for i in range(9):
        mr, mc = curR + dr[curD][i], curC + dc[curD][i]
        m = int(n * late[i])
        if 0 <= mr < N and 0 <= mc < N:
            A[mr][mc] += m
        else:
            result += m
        A[r][c] -= m
    if 0 <= ar < N and 0 <= ac < N:
        A[ar][ac] += A[r][c]
    else:
        result += A[r][c]
    A[r][c] = 0

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
curD = 0
curR = curC = N // 2
left, right = curC - 1, curC + 1
result = 0
while curR or curC:
    if curD == 0:
        tornado(curR, curC - 1, curR, curC - 2)
        curC -= 1
        if curC == left:
            curD = 1
    elif curD == 1:
        tornado(curR + 1, curC, curR + 2, curC)
        curR += 1
        if curR == right:
            curD = 2
    elif curD == 2:
        tornado(curR, curC + 1, curR, curC + 2)
        curC += 1
        if curC == right:
            curD = 3
    else:
        tornado(curR - 1, curC, curR - 2, curC)
        curR -= 1
        if curR == left:
            curD = 0
            left -= 1
            right += 1
print(result)