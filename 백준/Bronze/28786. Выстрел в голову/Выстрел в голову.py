n, m, a, b = map(int, input().split())
cur = tot = result = 0
while tot < n:
    if cur == 0:
        if min(n - tot, m) * b < a:
            cur = min(n - tot, m)
            result += min(n - tot, m) * b
        else:
            cur = m
            result += a
    else:
        cur -= 1
        tot += 1
        result += 1
print(result)