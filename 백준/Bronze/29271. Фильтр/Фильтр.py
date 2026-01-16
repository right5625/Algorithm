n, r, x = map(int, input().split())
cur = result = 0
for i in list(map(int, input().split())):
    cur = min(cur + i, r)
    result += min(cur, x)
    cur -= min(cur, x)
print(result)