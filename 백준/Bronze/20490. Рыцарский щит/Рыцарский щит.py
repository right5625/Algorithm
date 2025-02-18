a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
print(a1 + b1 + c1 + a2 + b2 + c2 - max(a1, b1, c1) - max(a2, b2, c2) + abs(max(a1, b1, c1) - max(a2, b2, c2)))