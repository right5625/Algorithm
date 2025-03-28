import math

while True:
    n, width, length, height, area, m = map(int, input().split())
    if n == width == length == height == area == m == 0:
        break
    s = 0
    for _ in range(m):
        w, h = map(int, input().split())
        s += w * h
    print(math.ceil(((width * length) + (width * height * 2) + (length * height * 2) - s) * n / area))