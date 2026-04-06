cur = result = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == b == 0:
        cur += 2
    else:
        result = max(result, cur)
        cur = 0
print(max(result, cur))