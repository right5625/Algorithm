R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
for r in range(R):
    if A[r][0] == -1:
        air1, air2 = r, r + 1
        break
for _ in range(T):
    B = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if A[r][c] > 0:
                cnt = 0
                for i in range(4):
                    mr, mc = r + dr[i], c + dc[i]
                    if 0 <= mr < R and 0 <= mc < C and A[mr][mc] != -1:
                        B[mr][mc] += A[r][c] // 5
                        cnt += 1
                A[r][c] -= A[r][c] // 5 * cnt
    for r in range(R):
        for c in range(C):
            A[r][c] += B[r][c]
    for r in range(air1 - 1, 0, -1):
        A[r][0] = A[r - 1][0]
    for c in range(C - 1):
        A[0][c] = A[0][c + 1]
    for r in range(air1):
        A[r][C - 1] = A[r + 1][C - 1]
    for c in range(C - 1, 1, -1):
        A[air1][c] = A[air1][c - 1]
    A[air1][1] = 0
    for r in range(air2 + 1, R - 1):
        A[r][0] = A[r + 1][0]
    for c in range(C - 1):
        A[R - 1][c] = A[R - 1][c + 1]
    for r in range(R - 1, air2, -1):
        A[r][C - 1] = A[r - 1][C - 1]
    for c in range(C - 1, 1, -1):
        A[air2][c] = A[air2][c - 1]
    A[air2][1] = 0
print(sum(sum(i) for i in A) + 2)