N, M, x, y, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
dice = [0] * 7
top, right, front, bottom, left, back = 1, 3, 5, 6, 4, 2
dx, dy = (0, 0, 0, -1, 1), (0, 1, -1, 0, 0)
for i in list(map(int, input().split())):
    mx, my = x + dx[i], y + dy[i]
    if 0 <= mx < N and 0 <= my < M:
        x, y = mx, my
        if i == 1:
            top, right, bottom, left = left, top, right, bottom
        elif i == 2:
            top, right, bottom, left = right, bottom, left, top
        elif i == 3:
            top, front, bottom, back = front, bottom, back, top
        else:
            top, front, bottom, back = back, top, front, bottom
        if A[x][y] == 0:
            A[x][y] = dice[bottom]
        else:
            dice[bottom] = A[x][y]
            A[x][y] = 0
        print(dice[top])