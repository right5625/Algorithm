r1, c1, r2, c2 = map(int, input().split())
A = [['' for _ in range(abs(c2 - c1) + 1)] for _ in range(abs(r2 - r1) + 1)]
dr, dc = (0, -1, 0, 1), (1, 0, -1, 0)
cur_r, cur_c, cur_n, boundary, idx, cnt = 0, 0, 1, 1, 0, 0
while cnt < (abs(r2 - r1) + 1) * (abs(c2 - c1) + 1):
    if r1 <= cur_r <= r2 and c1 <= cur_c <= c2:
        A[abs(r1 - cur_r)][abs(c1 - cur_c)] = str(cur_n)
        cnt += 1
    cur_r += dr[idx % 4]
    cur_c += dc[idx % 4]
    cur_n += 1
    if (idx % 4 == 0 and cur_c == boundary) or (idx % 4 == 1 and cur_r == -boundary) or (idx % 4 == 2 and cur_c == -boundary) or (idx % 4 == 3 and cur_r == boundary):
        idx += 1
        boundary = idx // 4 + 1
for i in range(abs(r2 - r1) + 1):
    for j in range(abs(c2 - c1) + 1):
        A[i][j] = ' ' * (len(str(cur_n)) - len(A[i][j])) + A[i][j]
for i in range(abs(r2 - r1) + 1):
    print(*A[i])