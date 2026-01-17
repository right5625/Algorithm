n, m = map(int, input().split())
x, y = map(int, input().split())
k = int(input())
result = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if 0 < abs(i - x) + abs(j - y) <= k:
            result += 1
print(result)