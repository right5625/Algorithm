while True:
    a = input().split()
    d, n = float(a[0]), int(a[1])
    if d == n == 0:
        break
    xy = [list(map(float, input().split())) for _ in range(n)]
    sour = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if (xy[i][0] - xy[j][0]) ** 2 + (xy[i][1] - xy[j][1]) ** 2 <= d * d:
                sour[i] = sour[j] = 1
    print(f"{sum(sour)} sour, {n - sum(sour)} sweet")