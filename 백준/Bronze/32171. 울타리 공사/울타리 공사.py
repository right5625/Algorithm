x1, y1, x2, y2 = 10, 10, -10, -10
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    x1, y1, x2, y2 = min(x1, a), min(y1, b), max(x2, c), max(y2, d)
    print(((x2 - x1) + (y2 - y1)) * 2)