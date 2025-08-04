a, b, c, d, e = map(int, input().split())
print(f'{max(0, d - max(1, c - b)) + max(0, c - a - e)} {b - a + 1 - (1 if d == e else 2)}')