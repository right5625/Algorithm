h, w, n = map(int, input().split())
result = [['.' for _ in range(w)] for _ in range(h)]
for i in range(n):
    r1, c1, r2, c2 = map(int, input().split())
    r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1
    for j in range(c1, c2 + 1):
        result[r1][j] = result[r2][j] = chr(ord('a') + i)
    for j in range(r1 + 1, r2):
        result[j][c1] = result[j][c2] = chr(ord('a') + i)
for i in range(h):
    print(*result[i], sep='')