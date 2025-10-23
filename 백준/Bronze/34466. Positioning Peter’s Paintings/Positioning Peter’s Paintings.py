A, B, X, Y = map(int, input().split())
print(min(((X + Y + B) * 2 if A < X else (A + B + Y) * 2), ((X + Y + A) * 2 if B < Y else (A + B + X) * 2)))