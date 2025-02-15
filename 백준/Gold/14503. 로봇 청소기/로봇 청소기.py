N, M = map(int, input().split())
r, c, d = map(int, input().split())
A = [list(map(int ,input().split())) for _ in range(N)]
vst = [[False for _ in range(M)] for _ in range(N)]
dr, dc = (-1, 0, 1, 0), (0, 1, 0, -1)
while True:
    if not vst[r][c]:
        vst[r][c] = True
    flag = False
    for i in range(4):
        mr, mc = r + dr[i], c + dc[i]
        if not A[mr][mc] and not vst[mr][mc]:
            flag = True
            break
    if flag:
        d = 3 if d == 0 else d - 1
        mr, mc = r + dr[d], c + dc[d]
        if not A[mr][mc] and not vst[mr][mc]:
            vst[mr][mc] = True
            r, c = mr, mc
    else:
        mr, mc = r - dr[d], c - dc[d]
        if not A[mr][mc]:
            r, c = mr, mc
        else:
            break
print(sum(i.count(True) for i in vst))