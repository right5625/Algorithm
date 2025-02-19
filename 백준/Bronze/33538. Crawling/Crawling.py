l = int(input())
n = int(input())
t = float(input())
res = 'DOOMED'
for _ in range(n):
    f, b = map(float, input().split())
    if l / f + l / b < t:
        res = 'HOPE'
print(res)