n = int(input())
a = list(map(int, input().split()))
res = 0
for i in range(n):
    x, y = map(int, input().split())
    if a[i]:
        res += max(y - x, 0)
print(res)