a, b, c, d = map(int, input().split())
res = [x for x in range(1, 4) if a ** x + b ** x + c ** x == d]
print(res[0] if len(res) == 1 else -1)