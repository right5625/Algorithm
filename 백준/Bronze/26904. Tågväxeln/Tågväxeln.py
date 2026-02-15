n, m = map(int, input().split())
s = False if n < m else True
result = 0
for i in range(1, 1440):
    if (i % n == i % m == 0) or (i % n == 0 and s) or (i % m == 0 and not s):
        s = not s
        result += 1
print(result)