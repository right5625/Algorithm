dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
for _ in range(int(input())):
    n = int(input())
    A = [list(map(int, input().split())) for _ in range(n)]
    result = 'NO'
    for r in range(n):
        for c in range(n):
            if A[r][c] == 0:
                result = 'YES'
            for i in range(4):
                mr, mc = r + dr[i], c + dc[i]
                if 0 <= mr < n and 0 <= mc < n and A[r][c] == A[mr][mc]:
                    result = 'YES'
    print(result)