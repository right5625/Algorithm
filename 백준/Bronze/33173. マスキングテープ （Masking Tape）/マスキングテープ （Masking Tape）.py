H, W, Q = map(int, input().split())
A = [[0 for _ in range(W)] for _ in range(H)]
B = [[False for _ in range(W)] for _ in range(H)]
dr, dc = (0, 0, 1, 1), (0, 1, 0, 1)
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        for i in range(4):
            mr, mc = q[1] + dr[i] - 1, q[2] + dc[i] - 1
            if not B[mr][mc]:
                A[mr][mc] = q[3]
    else:
        for i in range(4):
            mr, mc = q[1] + dr[i] - 1, q[2] + dc[i] - 1
            B[mr][mc] = True
for i in A:
    print(*i)