n, m = map(int, input().split())
cur, result = 1, 0
for i in list(map(int, input().split())):
    result += min(abs(i - cur), n - abs(i - cur))
    cur = i
print(result)