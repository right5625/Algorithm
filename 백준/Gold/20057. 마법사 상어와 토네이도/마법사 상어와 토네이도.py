N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
curR = curC = N // 2
left, right = curC - 1, curC + 1
d = 0
late = (0.05, 0.01, 0.07, 0.1, 0.02, 0.01, 0.07, 0.1, 0.02)
dr0, dc0 = (0, -1, -1, -1, -2, 1, 1, 1, 2), (-3, 0, -1, -2, -1, 0, -1, -2, -1)
dr1, dc1 = (3, 0, 1, 2, 1, 0, 1, 2, 1), (0, -1, -1, -1, -2, 1, 1, 1, 2)
dr2, dc2 = (0, -1, -1, -1, -2, 1, 1, 1, 2), (3, 0, 1, 2, 1, 0, 1, 2, 1)
dr3, dc3 = (-3, 0, -1, -2, -1, 0, -1, -2, -1), (0, -1, -1, -1, -2, 1, 1, 1, 2)
result = 0
while curR or curC:
    if d == 0:
        n = A[curR][curC - 1]
        for i in range(9):
            mr, mc = curR + dr0[i], curC + dc0[i]
            if 0 <= mr < N and 0 <= mc < N:
                A[mr][mc] += int(n * late[i])
            else:
                result += int(n * late[i])
            A[curR][curC - 1] -= int(n * late[i])
        if curC - 2 >= 0:
            A[curR][curC - 2] += A[curR][curC - 1]
        else:
            result += A[curR][curC - 1]
        A[curR][curC - 1] = 0
        curC -= 1
        if curC == left:
            d = 1
    elif d == 1:
        n = A[curR + 1][curC]
        for i in range(9):
            mr, mc = curR + dr1[i], curC + dc1[i]
            if 0 <= mr < N and 0 <= mc < N:
                A[mr][mc] += int(n * late[i])
            else:
                result += int(n * late[i])
            A[curR + 1][curC] -= int(n * late[i])
        if curR + 2 < N:
            A[curR + 2][curC] += A[curR + 1][curC]
        else:
            result += A[curR + 1][curC]
        A[curR + 1][curC] = 0
        curR += 1
        if curR == right:
            d = 2
    elif d == 2:
        n = A[curR][curC + 1]
        for i in range(9):
            mr, mc = curR + dr2[i], curC + dc2[i]
            if 0 <= mr < N and 0 <= mc < N:
                A[mr][mc] += int(n * late[i])
            else:
                result += int(n * late[i])
            A[curR][curC + 1] -= int(n * late[i])
        if curC + 2 < N:
            A[curR][curC + 2] += A[curR][curC + 1]
        else:
            result += A[curR][curC + 1]
        A[curR][curC + 1] = 0
        curC += 1
        if curC == right:
            d = 3
    else:
        n = A[curR - 1][curC]
        for i in range(9):
            mr, mc = curR + dr3[i], curC + dc3[i]
            if 0 <= mr < N and 0 <= mc < N:
                A[mr][mc] += int(n * late[i])
            else:
                result += int(n * late[i])
            A[curR - 1][curC] -= int(n * late[i])
        if curR - 2 >= 0:
            A[curR - 2][curC] += A[curR - 1][curC]
        else:
            result += A[curR - 1][curC]
        A[curR - 1][curC] = 0
        curR -= 1
        if curR == left:
            d = 0
            left -= 1
            right += 1
print(result)