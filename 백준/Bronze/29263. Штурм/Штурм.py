n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
result = 0
for r in range(n):
    for c in range(m):
        flag = True
        for i in range(4):
            mr, mc = r + dr[i], c + dc[i]
            if 0 <= mr < n and 0 <= mc < m and a[r][c] <= a[mr][mc]:
                flag = False
                break
        if flag:
            result += 1
print(result)