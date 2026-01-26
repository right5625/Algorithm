n, s = map(int, input().split())
cur, result = s, 0
for _ in range(n):
    x = input()
    x = int(x[0]) + 1 if len(x) == 2 else int(x)
    if cur >= x:
        cur -= x
    else:
        cur = s - x
        result += 1
print(result)